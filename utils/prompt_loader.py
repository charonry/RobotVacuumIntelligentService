"""
提示词加载
"""
from utils.config_handler import prompts_conf
from utils.path_tool import get_abs_path
from utils.logger_handler import logger

def load_prompts(prompt_path_key:str):
    try:
        prompt_path = get_abs_path(prompts_conf[prompt_path_key])
    except Exception as e:
        logger.error(f"在prompts.yml配置项中没有{prompt_path_key}配置项")
        raise e

    try:
        return open(prompt_path,"r",encoding="utf-8").read()
    except Exception as e:
        logger.error(f"解析{prompt_path}路径下系统提示词出错，{str(e)}")
        raise e

if __name__ == '__main__':
    print(load_prompts("main_prompt_path"))
    # print(load_prompts("rag_summarize_prompt_path"))
    # print(load_prompts("report_prompt_path1"))
