#1 вариант. Разработать БД «Турист» с тремя таблицами, установить связь между
#таблицами. Заполнить таблицы произвольными данными (не менее 10
#записей). Реализовать SQL-запросы на выборку, обновление, удаление
#данных из БД.

import sqlite3 as sq
from info import turi
from info import tu
from info import bro

#таблица туристов
with sq.connect('tur.db') as con:
  cur = con.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS turisti (
    id_турист INTEGER PRIMARY KEY AUTOINCREMENT,
    имя VARCHAR,
    фамилия VARCHAR,
    пол VARCHAR,
    дата_рождения DATE,
    номер_телефона VARCHAR,
    электронная_почта VARCHAR
  )""")
  #cur.executemany("INSERT INTO turisti VALUES (?, ?, ?, ?, ?, ?, ?)", turi)


#таблица туров
with sq.connect('tur.db') as con:
  cur = con.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS turi (
    id_тур INTEGER PRIMARY KEY AUTOINCREMENT,
    название VARCHAR,
    страна VARCHAR,
    город VARCHAR,
    дата_начала DATE,
    дата_окончания DATE,
    цена DECIMAL
  )""")
  #cur.executemany("INSERT INTO turi VALUES (?, ?, ?, ?, ?, ?, ?)", tu)

#таблица бронирования
with sq.connect('tur.db') as con:
  cur = con.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS bron (
    id_бронь INTEGER PRIMARY KEY AUTOINCREMENT,
    id_турист INTEGER FORGEIN KEY,
    id_тур INTEGER FORGEIN KEY,
    дата_бронирования DATE,
    кол_во туристов INTEGER
  )""")
  #cur.executemany("INSERT INTO bron VALUES (?, ?, ?, ?, ?)", bro)

#выборка
# with sq.connect('tur.db') as con:
#   cur = con.cursor()
#   cur.execute('SELECT * FROM turisti')
#   vse_turisti = cur.fetchall()

#   cur.execute('SELECT * FROM turi ORDER BY цена DESC')
#   ubivanie = cur.fetchall()

#   cur.execute('SELECT * FROM bron WHERE id_бронь=10')
#   gorod = cur.fetchall()

#   cur.execute("SELECT turisti.* FROM bron INNER JOIN turisti ON bron.[id_турист]=turisti.[id_турист] WHERE bron.[дата_бронирования] > '2022-12-01' ")
#   opred = cur.fetchall()

#   cur.execute('SELECT название, страна, город FROM turi')
#   strgor = cur.fetchall()

#   cur.execute("SELECT * FROM turisti WHERE дата_рождения > 1990-01-01 AND пол='ж'")
#   pol = cur.fetchall()

#   cur.execute('SELECT * FROM turi WHERE цена > 5000')
#   cena = cur.fetchall()

#   cur.execute("SELECT turisti.* FROM bron INNER JOIN turisti ON bron.[id_турист]=turisti.[id_турист] WHERE bron.[id_тур] = 6")
#   konkret = cur.fetchall()

#   cur.execute("SELECT turisti.* FROM bron INNER JOIN turisti ON bron.[id_турист]=turisti.[id_турист] WHERE bron.[дата_бронирования] = '2023-03-04' ")
#   data = cur.fetchall()

#   cur.execute("SELECT * FROM turisti WHERE номер_телефона LIKE '+7%'")
#   tel = cur.fetchall()
# print('1. Все туристы:', vse_turisti)
# print('2. Все туры в порядке убывания:', ubivanie)
# print('3. Все бронирования в заданном городе:', gorod)
# print('4. Все туристы, забронировавшие в опред период времени:', opred)
# print('5. Все туры с указанием страны и города:', strgor)
# print('6. Все туристы-женщины, рожденные позже 1990:', pol)
# print('7. Все туры, где цена больше 5000:', cena)
# print('8. Все туристы, забронировавшие конкертный тур:', konkret)
# print('9. Все турситы, забронировавшие тур в конкретную дату:', data)
# print('10. Все туристы, у которых номер тлф на +7:', tel)

#обновления
#with sq.connect('tur.db') as con:
     #cur = con.cursor()
     #cur.execute("UPDATE turi SET дата_начала = '2023-05-01' WHERE id_тур = 1 ")
     #cur.execute("UPDATE turi SET цена = 1500 WHERE id_тур = 7")
     #cur.execute("UPDATE turisti SET номер_телефона = '+1(555)123-4567' WHERE id_турист = 5")
     #cur.execute("UPDATE bron SET дата_бронирования = '2023-04-05' WHERE id_бронь = 3")
     #cur.execute("UPDATE bron SET кол_во = 3 WHERE id_бронь = 8")
     #cur.execute("UPDATE turi SET дата_окончания = '2023-08-31' WHERE id_тур = 2")
     #cur.execute("UPDATE turisti SET электронная_почта = 'new_email@example.com' WHERE id_турист = 1")
     #cur.execute("UPDATE turi SET дата_начала = '2023-06-15' WHERE id_тур = 4")
     #cur.execute("UPDATE turi SET дата_начала = '2023-05-01' WHERE страна = 'Испания'")
     #cur.execute("UPDATE turi SET цена = 1500 WHERE название = 'Греция - отдых на море'")
     #cur.execute("UPDATE turi SET дата_начала = '2023-06-01' WHERE название = 'Испания - путешествия по городам'")
     #cur.execute("UPDATE bron SET кол_во = 3 WHERE id_бронь = 2")
     #cur.execute("UPDATE turisti SET номер_телефона = '+1 (123) 456-7890' WHERE id_турист = 1")
     #cur.execute("UPDATE turi SET дата_начала = '2024-07-01' WHERE  цена < 2000 ")
     #cur.execute("UPDATE turisti SET электронная_почта = 'new_email@example.com' WHERE номер_телефона LIKE '+7%' ")
     #cur.execute("UPDATE turi SET дата_начала = '2023-08-15' WHERE id_тур in (SELECT id_тур FROM bron WHERE кол_во > 2)")
     #cur.execute("UPDATE turi SET название = 'Египет-отдых на курорте' WHERE id_тур in (SELECT id_тур FROM bron WHERE id_тур = 3 )")

#удаления
#with sq.connect('tur.db') as con:
    #cur = con.cursor()
    #cur.execute("DELETE FROM bron WHERE id_турист = 1")
    #cur.execute("DELETE FROM bron WHERE id_тур = 2")
    #cur.execute("DELETE FROM bron WHERE дата_бронирования = '2023-05-15'")
    #cur.execute("DELETE FROM turisti WHERE id_турист in (SELECT id_тур FROM bron WHERE id_тур = 3 )")
    #cur.execute("DELETE FROM bron WHERE id_турист in (SELECT id_турист FROM turisti WHERE номер_телефона = '+4(875)739-20-34' )")
    #cur.execute("DELETE FROM bron WHERE id_турист in (SELECT id_турист FROM turisti WHERE электронная_почта = 'vinograd@mail.ru' )")
    #cur.execute("DELETE FROM bron WHERE дата_бронирования > '2023-04-05'")
    #cur.execute("DELETE FROM turisti WHERE id_турист in (SELECT id_тур FROM bron WHERE id_тур = 5)")
    #cur.execute("DELETE FROM bron WHERE дата_бронирования < '2022-12-10'")
    #cur.execute("DELETE FROM bron WHERE id_тур in (SELECT id_тур FROM turi WHERE цена = 250000 )")