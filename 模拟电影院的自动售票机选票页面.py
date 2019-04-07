class Film:
    # 电影名
    FilmName = {
        1: "环太平洋，雷霆崛起",
        2: "头号玩家",
        3: "红海行动"
    }

    # 电影场次
    FilmCount = {
        "9:30", "10:40", "12:00"
    }

    # 座位
    FilmSeat = {
        "10-01", "10-02", "10-03", "10-04"
    }
    def __init__(self,FilmName,FilmCount,FilmSeat):
        self.FilmName=FilmName
        self.FilmCount=FilmCount
        self.FilmSeat=FilmSeat

    def Choice(self,name,count,seat):
        print("欢迎使用自动售票机~~~")
        print("")
        print("请选择正在上映的电影：1.《环太平洋，雷霆崛起》2.《头号玩家》3.《红海行动》")
        for i in Film.FilmName:
            if int(name)<0:
                print("已选电影:"+Film.FilmName[1])
                break
            elif int(name)>len(Film.FilmName):
                print("已选电影:"+Film.FilmName[1])
                break
            else:
                print("已选电影:"+Film.FilmName[name])
                break
        print("")
        print("请选择电影播放场次：1.9:30 2.10:40 3.12:00")
        if count in Film.FilmCount:
            print("已选择电影场次："+count)
        else:
            print("您选择的电影场次不在该电影院场次中")
        print("")
        print("请选择座位剩余座位：10-01,10-02,10-03,10-04")
        if seat in Film.FilmSeat:
            print("选择座位："+seat)
        else:
            print("您选择的座位已经被被人选择，请您重新选择")
        print("")

        print("电影："+Film.FilmName[name])
        print("播出时间："+count)
        print("座位："+seat)

f=Film(Film.FilmName,Film.FilmCount,Film.FilmSeat)

f.Choice(2,"10:40","10-01")