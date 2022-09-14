# 某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个 LED显示板做电影推荐，上面公布着影评和相关电影描述。
# 作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非boring(不无聊)的并且 id 为奇数的影片，结果请按等级 rating 排列
select * from cinema where description != "boring" and id % 2 = 1 order by rating desc