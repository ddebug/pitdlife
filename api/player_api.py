from typing import List
from flask import Flask, request, jsonify
from sqlmodel import SQLModel, create_engine, Session
from player_model import Player

# 初始化 Flask 应用
app = Flask(__name__)

# 设置数据库 URL，这里使用 SQLite 作为示例

engine = create_engine(DATABASE_URL)
if not engine.has_table("player"):
    SQLModel.metadata.create_all(engine)

# 创建玩家
@app.route('/players', methods=['POST'])
def create_player():
    player_data = request.json
    player = Player(**player_data)
    
    with Session(engine) as session:
        session.add(player)
        session.commit()
        session.refresh(player)
    
    return jsonify(player.dict()), 201

# 获取所有玩家
@app.route('/players', methods=['GET'])
def get_players():
    with Session(engine) as session:
        players = session.query(Player).all()
    
    return jsonify([player.dict() for player in players]), 200

# 获取单个玩家
@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id: int):
    with Session(engine) as session:
        player = session.query(Player).filter(Player.id == player_id).first()
    
    if player is None:
        return jsonify({"error": "Player not found"}), 404
    
    return jsonify(player.dict()), 200

# 更新玩家信息
@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id: int):
    player_data = request.json
    
    with Session(engine) as session:
        player = session.query(Player).filter(Player.id == player_id).first()
        if player is None:
            return jsonify({"error": "Player not found"}), 404
        
        for key, value in player_data.items():
            setattr(player, key, value)
        
        session.add(player)
        session.commit()
    
    return jsonify(player.dict()), 200

# 删除玩家
@app.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id: int):
    with Session(engine) as session:
        player = session.query(Player).filter(Player.id == player_id).first()
        if player is None:
            return jsonify({"error": "Player not found"}), 404
        
        session.delete(player)
        session.commit()
    
    return jsonify({"success": "Player deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
