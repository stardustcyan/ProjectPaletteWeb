from app import app, db
from app.models import Vtuber, Video, Group


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Vtuber': Vtuber, 'Video': Video, 'Group': Group}
