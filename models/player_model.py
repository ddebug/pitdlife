from typing import Optional
from sqlmodel import SQLModel, Field

# 定义 Player 类，作为玩家信息的数据模型，并继承 SQLModel 以使用 SQLModel 功能
    # 主键 id，类型为 Optional[int]，默认值为 None，将其设置为表的主键
    # 玩家姓名，类型为 str
    # 玩家性别，类型为 str
    # 玩家年龄，类型为 int
    # 玩家专业，类型为 str  major

    # 玩家的 San 值，类型为 int，默认值为 100  san_value  
    # 玩家的体力，类型为 int，默认值为 100 energy 
    # 导师好感度，类型为 int，默认值为 50  advisor_affection 
    # 论文完成度，类型为 int，默认值为 0  paper_progress 
    # 论文质量，类型为 int，默认值为 0 paper_quality 


class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    name: str = Field(sa_column=Column(String(255), nullable=False), title="name")
    gender: str = Field(sa_column=Column(String(255), nullable=False, default="女"), title="gender")
    age: int = Field(sa_column=Column(Integer, nullable=False, default=18), title="age")
    major: str = Field(sa_column=Column(String(255), nullable=False, default="未知"), title="major")
    san_value: int = Field(sa_column=Column(Integer, nullable=False, default=100), title="san_value")
    energy: int = Field(sa_column=Column(Integer, nullable=False, default=100), title="energy")
    advisor_affection: int = Field(sa_column=Column(Integer, nullable=False, default=50), title="advisor_affection")
    paper_progress: int = Field(sa_column=Column(Integer, nullable=False, default=0), title="paper_progress")
    paper_quality: int = Field(sa_column=Column(Integer, nullable=False, default=0), title="paper_quality")
    money: int = Field(sa_column=Column(Integer, nullable=False, default=0), title="money")
