import os, shutil, platform, argparse

def exe(str, platform):
    platform_to_extension = {
        "Windows": ".exe",
    }
    return str + platform_to_extension.get(platform, "")

present_working_platform = platform.system()
present_working_directory = os.getcwd().replace("\\", "/") + "/"
target_dir = present_working_directory + "target/"
frontend_dir = present_working_directory + "frontend/"
backend_dir = present_working_directory + "backend/"

def build(is_release):
    mode_dir = target_dir + ("release/" if is_release else "debug/")

    ## Target
    # Creating /target/run
    try:
        os.makedirs(mode_dir)
    except FileExistsError:
        pass
    # Cleaning everything in /target/run
    for filename in os.listdir(mode_dir):
        file_path = os.path.join(mode_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    ## Frontend
    print("Building frontend.")
    # Building frontend
    os.chdir(frontend_dir)
    os.system("npm install > " + os.devnull + " 2>&1")
    os.system("npm run build > " + os.devnull + " 2>&1")
    # Moving /frontend/build/ to /target/run/
    shutil.copytree(frontend_dir + "build", mode_dir + "page")

    ## Backend
    print("Building backend.")
    # Building backend
    os.chdir(backend_dir)
    os.system("cargo build " + ("--release " if is_release else "") +"> " + os.devnull + " 2>&1")
    # Moving /backend/target/debug/backend.exe to /target/run/server.exe
    shutil.copy(
        src = exe(backend_dir + "target/" + ("release" if is_release else "debug") + "/backend", present_working_platform), 
        dst = exe(mode_dir + "server", present_working_platform)
    )

def run(is_release):
    mode_dir = target_dir + ("release/" if is_release else "debug/")

    ## Execution
    print("Starting server.")
    os.chdir(mode_dir)
    os.startfile(exe(mode_dir + "server", present_working_platform))

def main():
    parser = argparse.ArgumentParser(description = "Run tasks.")
    parser.add_argument(
        "task",
        choices = ["build", "run"],
        help = "Task to run"
    )
    parser.add_argument(
        "--release", 
        action = "store_true", 
        help = "Run task in release mode"
    )
    args = parser.parse_args()

    # Debug
    print("Platform: " + present_working_platform)
    print("Directory: " + present_working_directory)
    print("")

    # Check
    has_missing = False
    if shutil.which("npm") is None:
        print("NodeJS is not installed on your system. https://nodejs.org/")
    if shutil.which("cargo") is None:
        print("Rust is not installed on your system. https://www.rust-lang.org/tools/install")
    if has_missing:
        print("Aborting process due to missing required tool(s).")
        return

    # Run task
    build(args.release)
    if args.task == "run":
        run(args.release)


if __name__ == "__main__":
    main()