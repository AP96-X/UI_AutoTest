import os
import pytest
from Config.Config import Config

if __name__ == '__main__':
    AllureReport = Config.test_report_dir
    AllureResult = Config.test_result_dir
    Screenshot = Config.test_screenshot_dir
    os.system(f"rm -rf {os.path.join(Screenshot,'*.png')}")
    # pytest.main(["-v", "-s", f'--alluredir={AllureResult}', "--clean-alluredir"])
    pytest.main(["-v", "-s", '--reruns=0', f'--alluredir={AllureResult}', "--clean-alluredir"])
    os.system(f'allure generate {AllureResult} -o {AllureReport} --clean')
