#[macro_use]
extern crate rocket;

use std::env;

use rocket::fs::{relative, FileServer, NamedFile};

#[get("/<_..>", rank = 2)]
async fn not_found_rewrite() -> Option<NamedFile> {
    NamedFile::open(relative!("../frontend/build/index.html"))
        .await
        .ok()
}

#[launch]
fn rocket() -> _ {
    let mut path = env::current_dir().unwrap();
    path.push("page");
    rocket::build()
        .mount("/", FileServer::from(path).rank(1))
        .mount("/", routes![not_found_rewrite])
}
