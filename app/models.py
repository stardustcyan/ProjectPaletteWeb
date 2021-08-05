# app/models.py
# 数据库模型

from app import db
from datetime import datetime


class Vtuber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    videos = db.relationship('Video', backref='liver', lazy='dynamic')
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    fans = db.Column(db.Integer)

    def __repr__(self):
        return '<Vtuber {}>'.format(self.name)


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(140))
    vtuber_id = db.Column(db.Integer, db.ForeignKey('vtuber.id'))
    face = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    title = db.Column(db.String(300))

    def __repr__(self):
        return '<Video {}>'.format(self.link)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vtubers = db.relationship('Vtuber', backref='group', lazy='dynamic')
    name = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<Group {}>'.format(self.name)
