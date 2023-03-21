<?php

// 读取前端传递的数据
$data = $_POST['data'];

// 将数据写入文件中
file_put_contents('save.dat', $data);

// 返回保存成功消息
echo '保存成功！';
