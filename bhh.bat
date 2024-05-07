python -Xutf8 manage.py dumpdata --natural-foreign --indent 2 --exclude=wagtailcore.Site -o db.json
 mv db.sqlite3 db.sqlite3.old
py manage.py migrate
python manage.py shell -c "from django.core.management.sql import sql_flush; from django.db import connection; print(sql_flush(connection, ['wagtailcore_site'], interactive=False));"
 python manage.py loaddata db.json
if [ $? -eq 0 ]; then
    mv db.sqlite3 db1.sqlite3

    mv db.sqlite3.old db.sqlite3 
fi
 mv db.sqlite3.old db.sqlite3 
