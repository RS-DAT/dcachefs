import pytest

from dcachefs.dcachefs import dCacheFileSystem


def test_initialize_fs_without_password():
    with pytest.raises(ValueError):
        dCacheFileSystem(
            username="user",
        )


def test_initialize_fs_with_both_auth_and_token():
    with pytest.raises(ValueError):
        dCacheFileSystem(username="user", password="pass", token="test_token")


def test_ls_without_api_url():
    fs = dCacheFileSystem(token="test_token")
    with pytest.raises(ValueError):
        fs.ls("/test")


def test_cat_without_webdav_url():
    fs = dCacheFileSystem(token="test_token")
    with pytest.raises(ValueError):
        fs.get("/test/test.txt", "test.txt")


def test_cat_with_webdav_url():
    fs = dCacheFileSystem(token="test_token")
    with pytest.raises(ValueError):
        fs.get("/test/test.txt", "test.txt")


def test_initialize_fs_without_webdav_url():
    fs = dCacheFileSystem(token="test_token")
    with pytest.raises(ValueError):
        fs.get("/test/test.txt", "test.txt")


def test_strip_protocol_removes_dcache_protocol():
    path = dCacheFileSystem._strip_protocol("dcache://a/b")
    assert path == "a/b"
    # Should also work on iterables
    paths = dCacheFileSystem._strip_protocol(["dcache://a/b", "dcache://b/c"])
    assert paths == ["a/b", "b/c"]


def test_strip_protocol_removes_webdav_port():
    path = dCacheFileSystem._strip_protocol("https://webdav.dcache.nl:8888/a/b")
    assert path == "/a/b"
    # Should also work on iterables
    paths = dCacheFileSystem._strip_protocol(
        ["https://webdav.dcache.nl:8888/a/b", "https://webdav.dcache.nl:8888/b/c"]
    )
    assert paths == ["/a/b", "/b/c"]


def test_get_kwargs_from_urls_parses_the_webdav_door():
    url = "https://webdav.dcache.nl:8888/a/b"
    kwargs = dCacheFileSystem._get_kwargs_from_urls(url)
    assert len(kwargs) == 1
    assert "webdav_url" in kwargs
    assert kwargs["webdav_url"] == "https://webdav.dcache.nl:8888"
    # Should also work on iterables
    urls = ["https://webdav.dcache.nl:8888/a/b", "https://webdav.dcache.nl:8888/b/c"]
    kwargs = dCacheFileSystem._get_kwargs_from_urls(urls)
    assert len(kwargs) == 1
    assert "webdav_url" in kwargs
    assert kwargs["webdav_url"] == "https://webdav.dcache.nl:8888"
