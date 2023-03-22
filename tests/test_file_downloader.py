from playwright.sync_api import Page


def test_file_downloader(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.locator("#content > div > a:nth-child(14)").click()
    download = download_info.value
    print(download.path())
