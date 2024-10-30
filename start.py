import os
import subprocess
from datetime import datetime

# 初始化变量
commit_date_1980 = datetime(2016, 6, 15, 12, 0, 0)
repo_path = r'D:\Github\green-test'

# 进入仓库目录
os.chdir(repo_path)

# 创建或修改文件用于提交
file_name = 'fakefile.txt'
with open(file_name, 'a') as f:
    f.write("Commit from 1980\n")

# 添加变更到暂存区
subprocess.run(['git', 'add', file_name])

# 提交并设置提交时间
formatted_date_2016 = commit_date_2016.strftime('%Y-%m-%dT%H:%M:%S')
commit_message_2016 = "Fake commit from 2016"
env = os.environ.copy()
env['GIT_COMMITTER_DATE'] = formatted_date_2016
subprocess.run(['git', 'commit', '--date', formatted_date_2016, '-m', commit_message_2016], env=env)

# 推送提交到 GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'main'])

print("Fake commit from 2016 created and pushed successfully.")
