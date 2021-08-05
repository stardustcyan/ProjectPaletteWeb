# app/routes.py
# 网站路径

from app import app, db
from app.models import Vtuber, Group, Video
from flask import render_template, request, url_for
import json

filename = 'data/Videoes.json'


@app.route('/')
@app.route('/index')
def index():
    vtbs = Vtuber.query.filter(Vtuber.id <= 10).all()

    return render_template('index.html', vtbs=vtbs, title='主页')


@app.route('/list')
def list():
    groups = Group.query.all()
    vtbs = Vtuber.query.all()

    return render_template('list.html', vtbs=vtbs, groups=groups, title='管人列表')


@app.route('/vtuber/<id>')
def vtuber(id):
    page = request.args.get('page', 1, type=int)
    vtb = Vtuber.query.filter_by(id=id).first_or_404()
    videos = Video.query.filter_by(vtuber_id=vtb.id).all()
    video_count = len(videos)

    return render_template('vtuber.html',\
        vtuber=vtb, videos=videos, title=vtb.name, video_count = video_count)


@app.route('/group/<id>')
def group(id):
    grp = Group.query.filter_by(id=id).first_or_404()
    vtbs = Vtuber.query.filter_by(group_id=id).all()

    return render_template('group.html', group=grp, vtubers=vtbs, title=grp.name)
