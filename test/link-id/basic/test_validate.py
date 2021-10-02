import util.config.config_util as cu
import util.linkage_agent.linkage_agent_util as lau


def test_validate():
    print("\nStarting test...")
    config = cu.get_config("test/link-id/basic/config.json")
    lau.validate(config)
    print("Done.")

