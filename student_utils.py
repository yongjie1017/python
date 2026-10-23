def parse_student(line):
    line = line.strip()
    if not line:
        raise ValueError("读到空行")
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数目错误，得到{len(parts)}个")
    name, score_str = parts
    name = name.strip()
    if len(name) == 0:
        raise ValueError("姓名为空")
    try:
        score = int(score_str.strip())
    except:
        raise ValueError("成绩不能转为整数")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩{score}超出0‑100范围")
    return {"name": name, "score": score}
