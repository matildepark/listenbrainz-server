from __future__ import absolute_import
from flask import Blueprint, render_template
from db.stats import get_last_submitted_recordings, get_stats

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def index():
    return render_template("index/index.html", stats=stats)
