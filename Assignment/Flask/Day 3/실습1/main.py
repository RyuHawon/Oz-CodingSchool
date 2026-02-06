from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./my_database.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(float, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime)

    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"

    def run_single():
        db = SessionLocal()

        # CREATE
        new_user = User(name="OZ_BE")
        db.add(new_user)
        db.commit()
        print("단일 사용자 추가:", new_user)
        
        # READ
        user = db.query(User).first()
        print("단일 사용자 찾음:", user)

        # UPDATE
        if user:
            user.name = "OZ_BE_Updated"
            db.commit()
            print("수정된 단일 사용자:", user)

            # DELETE
        if user:
            db.delete(user)
            db.commit()
            print("단일 사용자 삭제!")


        db.close()


    def run_bulk():
        db = SessionLocal()

        # CREATE
        new_users = {User(name="OZ_BE17"),User(name="OZ_BE18"), User(name="OZ_BE19")}
        for new_user in new_users:
            db.add(new_user)
        db.commit()
        print('복수 사용자 추가')

        # READ
        user = db.query(User).filter(User.name == 'OZ_BE17').first()
        print('조건조회: ', user)

        # 패턴 검색
        patterns = db.query(User).filter(User.name.like('BE_%')).all()
        print('패턴 검색: ', patterns)

        # UPDATE
        if patterns:
            for p in patterns:
                p.name = p.name + '_Updated'
            db.commit()
            print('복수 사용자 일괄 수정', patterns)


        db.close()
