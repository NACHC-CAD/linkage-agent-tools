import util.linkage_agent.linkage_agent_util as lau
import util.config.config_util as cu


def test_drop():
    print("\nStarting tests...")
    config = cu.get_config("test/link-id/basic/config.json")
    lau.drop(config)
    print("Done.")

