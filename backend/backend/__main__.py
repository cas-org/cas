import os
from typing import Tuple

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from .api.v1 import api as v1_api


class SinglePageApplication(StaticFiles):
    """Acts similar to the bripkens/connect-history-api-fallback
    NPM package."""

    def __init__(self, directory: os.PathLike, index='index.html') -> None:
        self.index = index

        # set html=True to resolve the index even when no
        # the base path is passed in
        super().__init__(directory=directory, packages=None, html=True, check_dir=True)

    async def lookup_path(self, path: str) -> Tuple[str, os.stat_result]:
        """Returns the index file when no match is found.

        Args:
            path (str): Resource path.

        Returns:
            [tuple[str, os.stat_result]]: Always retuens a full path and stat result.
        """
        full_path, stat_result = await super().lookup_path(path)

        # if a file cannot be found
        if stat_result is None:
            return await super().lookup_path(self.index)

        return (full_path, stat_result)


app = FastAPI()
app.mount(
    "/app",
    SinglePageApplication(
        directory="../frontend/build"),
    name="app")
app.include_router(v1_api.router)


@app.get("/")
def redirect_to_app():
    return RedirectResponse("/app/")
