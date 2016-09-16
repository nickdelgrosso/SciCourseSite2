from app import app, flatpages, LESSON_DIR, pygments_style_defs
from flask import render_template
from itertools import groupby



@app.route('/')
@app.route('/index')
def index():
    """Homepage"""
    lesson_pages = [p for p in flatpages if LESSON_DIR in p.path]
    lesson_pages = sorted(lesson_pages, key=lambda p: p.path)  # sort pages by filename
    days = groupby(lesson_pages,
                   lambda p: p.meta['day'])  # group pages into days [(0, [Page1, Page2]), (1, [Page3, Page4]),...]

    return render_template('landing.html', days=days)


@app.route('/lessons/<title>')
def lesson(title):
    """Lesson pages"""
    page = [p for p in flatpages if title in p.meta['title']][0]  # match title in FlatPages title tag list
    return render_template('lesson.html', page=page)

@app.route('/final_project')
def final_project():
    page = flatpages.get('final_project')
    return render_template('lesson.html', page=page)


@app.route('/pygments.css')
def pygments_css():
    """colors python code blocks in markdown text"""
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}



if __name__ == '__main__':
    app.run(debug=True)

