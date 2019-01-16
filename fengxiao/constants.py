
tb_name = "account"
sql_list = [
    "select * from {tb_name} order by id desc limit 1",
    "delete from {tb_name} order by id desc limit 1",
]
for i in sql_list:
    i = i.format(tb_name=tb_name)
    for j in range(len(sql_list)):
        sql_list[j] = i
# print(sql_list)

