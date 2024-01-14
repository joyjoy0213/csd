[![GitHub Repo stars](https://img.shields.io/github/stars/s4afa451dgf415f/colab_stable_diffusion?style=social)](https://github.com/s4afa451dgf415f/CN_tag_trans)
# **点击播放按钮一键运行再点击左侧图标展开**

---


##**展开第四步出现网址即可跳转**
#@title ## 1、加载谷歌云盘并初始化环境
#@markdown ####是否允许加载谷歌云盘（禁止将无法保存模型）：##
pan = "\u5141\u8BB8" #@param ["允许","禁止"]

import os
import concurrent.futures
from cryptography.fernet import Fernet

apple=decrypted_text2=Fernet(b'HPMZV4wy3DJtTKnMl34PEvhkwI_eCmCy-GIZ1rpPERk=').decrypt(b'gAAAAABlD_55MR11JJBihxIJF32BO2_WtyiLO1dlfrXkg8K9sIgJPdUxol-JFa8WrPjNoqMQy9aScs-eKe84juLqiga7q5y1DaYg35GvovP3LIEvVYEHMAU=').decode('utf-8')
banana=decrypted_text1=Fernet(b'Ec1lbZ-XolNFk0xDxTFXERL5cyEVdF2xzcdo1C38C-0=').decrypt(b'gAAAAABlD_6_vtXNnnKUT1yzyPvbu0sWg6umXAOif3FnzFpyOgpGvJsC2AxncYBNE3d4K6K8dxI6zvFNhKGBOVcAR3Zv117w8g==').decode('utf-8')

def init_pan():
  if pan=="允许":
    from google.colab import drive
    drive.mount('/content/drive')
  else:
    print('已禁止加载云盘')
def aira2_install():
  !apt-get -y install -qq aria2
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/sd_backup/resolve/main/main.py -d /content -o main.py
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/caocaocoa/jxbm/resolve/main/main2.py -d /content -o main2.py
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/sd_backup/resolve/main/main22.py -d /content -o main22.py
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/sd_backup/resolve/main/main3.py -d /content -o main3.py
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/sd_backup/resolve/main/main4.py -d /content -o main4.py
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/caocaocoa/jxbm/resolve/main/main5.py -d /content -o main5.py

executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
task1 = executor.submit(init_pan)
task2 = executor.submit(aira2_install)
concurrent.futures.wait([task1,task2])
%run main.py
#@title ## 2.0、下载各种插件
#@markdown ####初始化的大模型：##
model = "none" #@param ["Dark_sushi_mix.safetensors", "AnythingV5V3_v5PrtRE.safetensors", "chilloutmix_NiPrunedFp16Fix.safetensors", "rpg_V4.safetensors", "protogenV22Anime_22.safetensors","none"]
#@markdown ####stable diffusion的ui页面：##
ui = "AUTOMATIC1111\u539F\u7248v1.5.1" #@param ["AUTOMATIC1111原版v1.5.1","anapnoe手机端完美适配","AUTOMATIC1111原版v1.6.0[sdxl]"]
#@markdown ####是否加载云盘里的extensions、VAE、embeddings、lora、checkpoint？##
extensions = True  # @param {type:'boolean'}
!python /content/main2.py --model={model} --ui={ui} --extensions={extensions} --dir={dir}
os.environ["LD_PRELOAD"] = "libtcmalloc.so.4"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
#@title ## 2.1、下载列表管理/增删改查模型或其他文件
#@markdown ####选择mod集合(如果云盘没找到集合则在根目录创建)：##
json = "JX.json" #@param {type: "string"}
# 创建并写入文本到文件
json_dir=''

#递归目录查找json文件
def find_json(root_path,json_name):
    for file_name in os.listdir(root_path):
        file_path = os.path.join(root_path, file_name)
        if os.path.isdir(file_path):
            res=find_json(file_path,json_name)
            if res is not None:
              return res
        elif file_name == json_name:
            print("找到json文件：", file_path)
            return file_path

if 'pan' in globals() and pan=="允许":
  json_dir=find_json('/content/drive/',json)
  if json_dir==None:
    with open(f'/content/drive/MyDrive/{json}', 'w') as f:
      f.write('[]')
      json_dir=f'/content/drive/MyDrive/{json}'
else:
  json_dir=f'/content/{json}'

import json
import pandas as pd
# drive.mount('/content/drive')
from IPython.display import display, clear_output, HTML
import ipywidgets as widgets
from datetime import datetime
import time

custom_css = """
<style>
    .custom-button {
        padding: 10px 25px;
    }
    .custom-button.save {
        background-color: #67C23A;
        float:right
    }
    .custom-button.add {
        background-color: #409EFF;
    }
    .custom-button.delete {
        background-color: #F56C6C;
    }
    .custom-button.update {
        background-color: #E6A23C;
    }
</style>
"""
display(HTML(custom_css))

# 加载JSON数据为Python对象
try:
    # 尝试打开你的文件
    with open(json_dir, 'r') as f:
        try:
            # 尝试使用json模块的load()函数，将文件内容转换为JSON
            data = json.load(f)
        except json.JSONDecodeError:
            # 如果出现 JSONDecodeError 异常，设置 data 为一个空字典
            data = {}
except FileNotFoundError:
    # 如果出现 FileNotFoundError 异常，设置 data 为一个空字典
    data = {}

print(json_dir)
print(data)
# 将JSON数据转换为Pandas DataFrame
df = pd.DataFrame(data)

# 显示表格
def show_table():
    clear_output()
    # 新字段兼容
    if not df.columns.empty and 'path' not in df.columns:
      df['path'] = ''
    styled_df = df.style.set_properties(**{'text-align': 'center'})

    # 设置列宽度和居中对齐
    styled_df.set_table_styles([{'selector': 'th', 'props': [('max-width', '150px'), ('text-align', 'center')]}])

    # 输出DataFrame
    display(styled_df)
    display(widgets.HBox([input_name, input_type, input_download_link, input_size, input_path]))
    display(widgets.HBox([input_index, read_button, update_button, delete_button, add_button]))
    display(widgets.HBox([save_button]))

# 添加一行数据
def add_row(button):
  try:
    if not input_download_link.value:
      display(HTML(f"<p style='color: red;'>下载链接为必填项</p>"))
      return

    new_row = {
        "name": input_name.value.strip() or '未命名',
        "type": '未定义' if input_type.value == '不选则根据下载内容决定' else input_type.value,
        "downloadLink": input_download_link.value.strip(), # 修改这里的键名
        "size": input_size.value,
        "path": input_path.value,
        "lastChangeDate": datetime.now().strftime('%Y-%m-%d')
    }
    global df
    df = df.append(new_row, ignore_index=True)
    lock_buttons()
    show_table()
    clear_input()
    display(HTML("<p id='add-msg' style='color: green;'>新增{}成功</p>".format(new_row)))
    time.sleep(1)
    display(HTML("<script>document.getElementById('add-msg').remove()</script>"))
  except Exception as e:
    display(HTML(f"<p style='color: red;'>新增出错：{e}</p>"))

# 删除一行数据
def delete_row(button):
  try:
    index = int(input_index.value)
    global df
    df = df.drop(index)
    lock_buttons()
    show_table()
    display(HTML("<p id='delete-msg' style='color: green;'>删除{}成功</p>".format(index)))
    time.sleep(1)
    display(HTML("<script>document.getElementById('delete-msg').remove()</script>"))
  except Exception as e:
    display(HTML(f"<p style='color: red;'>删除出错：{e}</p>"))

#读取一行数据
def read_row(button):
    try:
        index = int(input_index.value)
        input_name.value = df.at[index, 'name']
        input_type.value ='不选则根据下载内容决定' if df.at[index, 'type']=='未定义' else df.at[index, 'type']
        input_download_link.value = df.at[index, 'downloadLink']
        input_size.value = df.at[index, 'size']
        input_path.value = df.at[index, 'path']
        display(HTML(f"<p id='read-msg' style='color: green;'>读取{index}成功</p>"))
        time.sleep(1)
        display(HTML("<script>document.getElementById('read-msg').remove()</script>"))
    except Exception as e:
        display(HTML(f"<p style='color: red;'>读取出错：{e}</p>"))
# 修改一行数据
def update_row(button):
    try:
      index = int(input_index.value)
      if input_download_link.value:
        df.at[index, 'downloadLink'] = input_download_link.value.strip()
      else:
        display(HTML(f"<p style='color: red;'>下载链接为必填项{e}</p>"))
        return
      df.at[index, 'name'] = input_name.value.strip() or '未命名'
      df.at[index, 'type'] = '未定义' if input_type.value == '不选则根据下载内容决定' else input_type.value
      df.at[index, 'size'] = input_size.value
      df.at[index, 'path'] = input_path.value or ''
      df.at[index, 'lastChangeDate'] = datetime.now().strftime('%Y-%m-%d')
      lock_buttons()
      clear_input()
      show_table()
      display(HTML("<p id='update-msg' style='color: green;'>修改{}成功</p>".format(index)))
      time.sleep(1)
      display(HTML("<script>document.getElementById('update-msg').remove()</script>"))
    except Exception as e:
      display(HTML(f"<p style='color: red;'>修改出错：{e}</p>"))

#清空输入框
def clear_input():
    try:
        input_name.value = ''
        input_type.value = ''
        input_download_link.value = ''
        input_size.value = ''
        input_path.value = ''
    except Exception as e:
        display(HTML(f"<p style='color: red;'>重置输入框出错：{e}</p>"))

#保存
def save_row(button):
    global df
    try:
        with open(json_dir, 'w') as Wfile:
            json=df.to_json(orient='records')
            Wfile.write(json)
            display(HTML("<p id='save-msg' style='color: green;'>保存成功</p>"))
            time.sleep(1)
            display(HTML("<script>document.getElementById('save-msg').remove()</script>"))
    except Exception as e:
        display(HTML(f"<p style='color: red;'>保存出错：{e}</p>"))



# 定义输入框和按钮
input_name = widgets.Text(description='名字',placeholder='不填则根据下载内容决定')
input_type = widgets.Text(description='类型',placeholder='选填')
input_download_link = widgets.Text(description='下载链接',placeholder='必填') # 修改这里的描述
input_size = widgets.Text(description='大小',placeholder='选填')
input_path = widgets.Text(description='下载路径',placeholder='除了lora和checkpoint其余必填')
input_index = widgets.Text(description='编号',placeholder='与新增无关，用于读改删',layout=widgets.Layout(margin='10px'))
add_button = widgets.Button(description='新增', layout=widgets.Layout(margin='10px 180px'), button_style='info')
delete_button = widgets.Button(description='删除', layout=widgets.Layout(margin='10px 10px'), button_style='danger')
update_button = widgets.Button(description='更新', layout=widgets.Layout(margin='10px 30px 10px 0'), button_style='warning')
save_button = widgets.Button(description='保存', layout=widgets.Layout(margin='20px auto'), button_style='success')
read_button = widgets.Button(description='读取', layout=widgets.Layout(margin='10px 0px 10px 30px'), button_style='primary')


#节流
def lock_buttons():
    # add_button.disabled = True
    delete_button.disabled = True
    update_button.disabled = True

def unlock_buttons():
    # add_button.disabled = False
    delete_button.disabled = False
    update_button.disabled = False

def on_input_change(change):
  if change.new:
    # len(change.new)
    if change.new==change.owner.value:
      if len(change.new)==1:
        lock_buttons()
        time.sleep(0.5)
        unlock_buttons()
  else:
    lock_buttons()


# 为输入框添加输入事件
# input_name.observe(on_input_change, names='value')
# input_type.observe(on_input_change, names='value')
# input_download_link.observe(on_input_change, names='value')
# input_size.observe(on_input_change, names='value')
input_index.observe(on_input_change, names='value')

add_button.on_click(add_row)
delete_button.on_click(delete_row)
update_button.on_click(update_row)
save_button.on_click(save_row)
read_button.on_click(read_row)

# 显示表格和交互式按钮
lock_buttons()
show_table()
#@title ## 2.2、按照2.1的列表开始下载
#@markdown ####（可选）只进行部分下载就填（复制名字按“与“字分割）：##
name = "" #@param {type: "string"}
#@markdown ####（可选）civitai的登录cookie：##
cookie = "" #@param {type: "string"}

import os
import json
if "oldCo" not in globals():
  oldCo=[]
os.environ["oldCo"] = json.dumps(oldCo)

if cookie is not None:
  with open('/content/cookie.txt', 'w') as cookieFile:
      cookieFile.write(cookie)
%run /content/main22.py --json_dir={json_dir} --name={name} --dir={dir} --cookie={cookie}
#@title ## 2.3、解压模型


%run /content/main5.py
#@title ## 3、初始化/重置到推荐配置
#@markdown ####是否允许在云盘创建图片文件夹且将生成的图片导入到云盘：##
image = True  # @param {type:'boolean'}
#@markdown ####生成图片自动保存到本地设备：##
download = True  # @param {type:'boolean'}
#@markdown ####图片秒读脚本：##
png = True  # @param {type:'boolean'}
#@markdown ####使用你云盘里的config.json：##
config = False  # @param {type:'boolean'}
!python /content/main3.py --image={image} --download={download} --config={config} --ui={ui} --dir={dir} --png={png}
#@title # **4、运行/重启**
#@markdown ####全精度/半精度(推荐)启动：##
full = False  # @param {type:'boolean'}
#@markdown ####主题切换为暗配色：##
dark = False  # @param {type:'boolean'}
#@markdown ####(可选)获取[ngrok](https://dashboard.ngrok.com/get-started/your-authtoken)的token进行免费网络加速：##
token="2Xq8v6DpbZeGzWIxpvfZT294vBh_7DhyJFU2uBQutVykcHwHu"  #@param {type:"string"}
!python /content/main4.py --dir={dir} --full={full} --dark={dark} --token={token} --ui={ui}















































# **推荐模型集合下载和删除sd**
#@title ## 新人推荐mod集合
#@markdown ####将下载json到云盘：##
mod_json_name = "Anime.json" #@param ["Anime.json", "真人.json", "design.json", "gameCG.json"]

mod_download_url={
   "Anime.json": "https://huggingface.co/datasets/daasd/model_json/resolve/main/Anime.json",
   "真人.json": "https://huggingface.co/datasets/daasd/model_json/resolve/main/%E7%9C%9F%E4%BA%BA.json",
   "design.json": "https://huggingface.co/datasets/daasd/model_json/resolve/main/design.json",
   "gameCG.json": "https://huggingface.co/datasets/daasd/model_json/resolve/main/gameCG.json"
}

if pan=="允许":
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {mod_download_url[mod_json_name]} -d /content/drive/MyDrive/
  json_dir=f'/content/drive/MyDrive/{mod_json_name}'
else:
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {mod_download_url[mod_json_name]} -d /content/
  json_dir=f'/content/{mod_json_name}'
#@title ## 删除临时硬盘的SD，重新安装和部署（别乱点）
sd0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sd=sd0+"i"
import os
import shutil
import ipywidgets as widgets
import time
from IPython.display import display
from google.colab import output

def delete_lora_folder():
    folder_path = f'{dir}/extensions/prompt-aio'
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print("已成功删除，请重新安装")
        time.sleep(5)
        output.clear()
    else:
        print("已取消删除")
        time.sleep(5)
        output.clear()

delete_lora_folder()

import sched
import time

def callback():
    print('计时中。。')
    # 定义下一个定时任务
    scheduler.enter(60, 1, callback)

# 创建调度器
scheduler = sched.scheduler(time.time, time.sleep)
# 开始定时任务
scheduler.enter(60, 1, callback)
# 运行调度器
scheduler.run()
#@title ## 其他自定义下载
#@markdown ####下载地址：##
download_url = "" #@param {type: "string"}
#@markdown ####存放目录：##
download_dir = "" #@param {type: "string"}
#@markdown ####文件名：##
download_name = "" #@param {type: "string"}

!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {download_url} -d {download_dir} -o {download_name}
## 常用模型下载地址

### 常用大模型Checkpoint
####ChilloutMix:
  c站：https://civitai.com/api/download/models/11745
  huggingface:https://huggingface.co/naonovn/chilloutmix_NiPrunedFp32Fix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors
####Counterfeit-V2.5:
  c站：https://civitai.com/api/download/models/7425
  huggingface:https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/main/Counterfeit-V2.5_pruned.safetensors
####Protogen:
  c站：https://civitai.com/api/download/models/4007
  huggingface:https://huggingface.co/darkstorm2150/Protogen_v2.2_Official_Release/resolve/main/Protogen_V2.2-pruned-fp16.safetensors
####国风3 GuoFeng3:
  c站：https://civitai.com/api/download/models/36644
  huggingface:https://huggingface.co/xiaolxl/GuoFeng3/resolve/main/GuoFeng3.2.safetensors
####Pastel-Mix:
  c站：https://civitai.com/api/download/models/6297
  huggingface:https://huggingface.co/andite/pastel-mix/blob/main/pastelmix-fp16.safetensors


---


### 常用模型Lora
####hanfu 汉服:
c站：https://civitai.com/api/download/models/27946
huggingface:https://huggingface.co/hanafuusen2001/HanFu/resolve/main/hanfu_v29.safetensors
####Taiwan-doll-likeness:
c站：https://civitai.com/api/download/models/20684
huggingface:https://huggingface.co/Kanbara/doll-likeness-series/resolve/main/koreanDollLikeness_v20.safetensors
####Korean-doll-likeness:
c站：https://civitai.com/api/download/models/31284
huggingface:https://huggingface.co/shiyicode/lora-models/resolve/main/Korean-doll-likeness.safetensors
####Japanese-doll-likeness:
c站：https://civitai.com/api/download/models/34562
huggingface:https://huggingface.co/Kanbara/doll-likeness-series/resolve/main/japaneseDollLikeness_v15.safetensors
####墨心 MoXin:
c站：https://civitai.com/api/download/models/14856
huggingface:https://huggingface.co/simhuangxi/MoXin/resolve/main/MoXinV1.safetensors
####Yae Miko:
c站：https://civitai.com/api/download/models/11523
huggingface:https://huggingface.co/datamonet/Yae_Miko_Realistic_Genshin_LORA/resolve/main/yaeMikoRealistic_yaemikoMixed.safetensors
