#[macro_use]
extern crate rocket;

use rocket::fs::{relative, FileServer, NamedFile};

#[get("/<_..>", rank = 2)]
async fn not_found_rewrite() -> Option<NamedFile> {
    NamedFile::open(relative!("../frontend/build/index.html"))
        .await
        .ok()
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount(
            "/",
            FileServer::from(relative!("../frontend/build")).rank(1),
        )
        .mount("/", routes![not_found_rewrite])
}
