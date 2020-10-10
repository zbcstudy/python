## conda版本查看
conda -V
conda --version 
 
## 更新
conda update conda           #更新conda
conda update anaconda        #更新anaconda
conda update anaconda-navigator    #update最新版本的anaconda-navigator   
 
## 查看已安装的虚拟环境
conda env list 
conda info -e
conda info --env
 
## conda -create -n env_name list_of_packages
## env_name是需要创建的环境名称，list_of_packages是在新环境中需要安装的工具包，有多个时用空格隔开
## 创建一个名为的环境，指定Python版本是3.5（conda会自动寻找3.5.x中的最新版本）
 
conda create -n xxxx python=3.5
conda create --name xxxx python=3.5  
 
conda activate xxxx           #开启xxxx环境
conda deactivate              #关闭环境
 
## 克隆环境，我想创建一个新环境BBB，完全克隆AAA的环境配置
conda create -n BBB --clone AAA
 
## 删除一个已有的环境
conda remove -n xxxx --all
 
## 环境重命名
## conda没有重命名的命令，所以可以先 clone 一个环境，然后删除原有的环境


# 查看当前环境下已安装的包
conda list
 
# 查看某个指定环境（xxxxx）下已安装的包
conda list -n xxxxx
 
# 查找package信息，例如查找numpy包信息，会列numpy的所有版本
conda search numpy
 
# 安装package，安装多个包用空格隔开
# 如果不用-n指定环境名称，则被安装在当前活跃环境
# 也可以通过-c指定通过某个channel安装
conda install -n xxxxx numpy pandas
 
# 更新package
conda update numpy           # 更新numpy（当前活跃的环境）  
conda update -n xxxxx numpy  # 更新指定xxxxx环境下的numpy
conda update python          # 假设当前环境是python3.4, conda会将python升级为3.4.x系列的最新版本
 
# 删除环境package
conda uninstall numpy
conda remove numpy           # 删除numpy包（当前活跃的环境）
conda remove -n xxxxx numpy  # 删除xxxxx环境下的包