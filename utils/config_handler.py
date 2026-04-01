"""
配置文件统一加载
"""
import yaml
from utils.path_tool import get_abs_path

def load_config(config_path, encoding: str="utf-8"):
    with open(get_abs_path(config_path),"r",encoding=encoding) as f:
        return yaml.load(f,Loader=yaml.FullLoader)


rag_conf = load_config("config/rag.yml")
chroma_conf = load_config("config/chroma.yml")
prompts_conf = load_config("config/prompts.yml")
agent_conf = load_config("config/agent.yml")

if __name__ == '__main__':
    print(rag_conf["chat_model_name"])
    print(chroma_conf["collection_name"])
    print(prompts_conf["main_prompt_path"])
    print(agent_conf["external_data_path"])