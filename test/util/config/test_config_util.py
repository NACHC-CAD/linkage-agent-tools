import util.config.config_util as cu


def test_get_config_with_rel_path():
    print("\nStarting test")
    cu.get_config("test/util/config/config.json")
    print("Done.")