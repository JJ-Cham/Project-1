from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)

    plants = relationship("Plant", back_populates="user")
    actions = relationship("Action", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    plant_name = Column(String, nullable=False)

    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    stage = Column(String, default="Seed")

    user = relationship("User", back_populates="plants")

    def __repr__(self):
        return (
            f"<Plant(id={self.id}, "
            f"name='{self.plant_name}', "
            f"stage='{self.stage}')>"
        )


class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    action_type = Column(String, nullable=False)

    carbon_saved = Column(Float, default=0)

    user = relationship("User", back_populates="actions")

    def __repr__(self):
        return (
            f"<Action(id={self.id}, "
            f"type='{self.action_type}', "
            f"carbon_saved={self.carbon_saved})>"
        )