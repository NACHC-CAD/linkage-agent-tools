from dcctools.config import Configuration
import validate
import util.config.config_util as cu



def test_validate():
    print("\nStarting test...")
    config = cu.get_config("test/link-id/basic/config.json")
    validate.validate(config)
    print("Done.")

