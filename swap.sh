#!/bin/bash

# 切换到目标目录
cd /Users/luogan/Desktop/大四上/文件存放/个人主页/images

# 定义文件名
FILE1="android-chrome-512x512.png"
FILE2="android-chrome-192x192.png"
BACKUP1="${FILE1}.backup"
BACKUP2="${FILE2}.backup"

# 检查文件是否存在
if [[ ! -f "$FILE1" ]] || [[ ! -f "$FILE2" ]] || [[ ! -f "$BACKUP1" ]] || [[ ! -f "$BACKUP2" ]]; then
    echo "错误: 某些文件不存在！"
    exit 1
fi

# 使用临时文件进行交换
echo "开始交换文件..."

# 交换 512x512
mv "$FILE1" temp_512.tmp
mv "$BACKUP1" "$FILE1"
mv temp_512.tmp "$BACKUP1"
echo "✓ 已交换 $FILE1 和 $BACKUP1"

# 交换 192x192
mv "$FILE2" temp_192.tmp
mv "$BACKUP2" "$FILE2"
mv temp_192.tmp "$BACKUP2"
echo "✓ 已交换 $FILE2 和 $BACKUP2"

echo "所有文件交换完成！"