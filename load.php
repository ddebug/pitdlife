<?php

// 从文件中读取数据并返回给前端
$data = file_get_contents('save.dat');
echo $data;
