from flask import *
from ahp import AHP_class

app = Flask(__name__)

@app.route("/first", methods=["POST", "GET"])
def original():
    if request.method == "POST":
        S = int(request.form["season"])
        D = request.form["departure"]
        return render_template("form2.html", S=S, D=D)
    else:
        return render_template("form1.html")

result_list = []
@app.route("/second", methods=["POST", "GET"])
def index1():
    if request.method == "POST":
        AHP = AHP_class()
        S = int(request.form["S"])
        D = request.form["D"]
        H = []
        for h in ["コスト", "グルメ", "スポット", "宿", "快適さ"]:
            H.append(int(request.form[h]))
        m_item = AHP.matrix(H, 5)
        an = AHP.weight(m_item, 5)
        if D == "北海道・東北":
            Ha = [1, 2, 4, 3, 7, 5, 6, 8, 9, 11, 12, 10, 13]
        elif D == "関東":
            Ha = [13, 4, 2, 1, 9, 3, 5, 6, 7, 8, 11, 10, 12]
        elif D == "東海":
            Ha = [13, 10, 8, 5, 9, 2, 1, 3, 4, 6, 7, 11, 12]
        elif D == "近畿":
            Ha = [12, 9, 11, 8, 13, 6, 4, 2, 1, 3, 5, 7, 10]
        elif D == "中国・四国":
            Ha = [13, 10, 11, 9, 12, 7, 6, 5, 4, 2, 1, 3, 8]
        else:
            Ha = [11, 10, 13, 9, 12, 8, 7, 6, 5, 4, 3, 1, 2]
        if S >= 3 and S <= 5:#春
            #グルメ
            Hb = [11, 10, 2, 3, 12, 1, 5, 8, 9, 4, 7, 6, 13]
            #スポット
            Hc = [1, 9, 13, 11, 4, 12, 7, 6, 5, 10, 8, 2, 3]
            #宿
            Hd = [2, 5, 3, 1, 4, 7, 13, 8, 12, 11, 9, 10, 6]
            #快適さ
            He = [13, 12, 3, 2, 11, 1, 5, 6, 4, 7, 8, 9, 10]
        elif S >= 6 and S <= 8:#夏
            Hb = [2, 13, 10, 9, 11, 8, 12, 7, 3, 6, 5, 4, 1]
            Hc = [2, 8, 12, 10, 13, 11, 6, 5, 4, 9, 7, 3, 1]
            Hd = [2, 8, 9, 6, 7, 11, 12, 3, 13, 4, 5, 10, 1]
            He = [1, 2, 4, 5, 3, 6, 7, 13, 12, 10, 8, 11, 9]
        elif S >= 9 and S <= 11:#秋
            Hb = [2, 3, 9, 10, 5, 6, 11, 4, 12, 8, 1, 7, 13]
            Hc = [3, 4, 12, 10, 11, 8, 6, 1, 9, 7, 2, 5, 13]
            Hd = [1, 4, 8, 7, 3, 6, 12, 2, 13, 9, 5, 11, 10]
            He = [13, 11, 9, 10, 12, 1, 3, 8, 7, 6, 4, 5, 2]
        else:#冬
            Hb = [1, 4, 11, 12, 3, 5, 10, 8, 7, 9, 6, 2, 13]
            Hc = [1, 3, 4, 6, 2, 11, 12, 9, 5, 7, 8, 10, 13]
            Hd = [3, 4, 2, 5, 1, 6, 12, 7, 11, 10, 9, 8, 13]
            He = [12, 11, 10, 7, 13, 1, 4, 9, 8, 6, 5, 3, 2]
        #マトリックス作成
        ma = AHP.matrix(Ha, 13)
        mb = AHP.matrix(Hb, 13)
        mc = AHP.matrix(Hc, 13)
        md = AHP.matrix(Hd, 13)
        me = AHP.matrix(He, 13)
        #幾何平均による各案の評価値計算
        an_a = AHP.weight(ma, 13)
        an_b = AHP.weight(mb, 13)
        an_c = AHP.weight(mc, 13)
        an_d = AHP.weight(md, 13)
        an_e = AHP.weight(me, 13)

        result = [value for value in AHP.final(an, an_a, an_b, an_c, an_d, an_e)]
        result_list.append(result)
        return render_template("form3.html", S=S, D=D)
    else:
        return render_template("form2.html")
@app.route("/third", methods=["POST", "GET"])
def index2():
    if request.method == "POST":
        AHP = AHP_class()
        S = int(request.form["S"])
        D = request.form["D"]
        H = []
        for h in ["コスト", "グルメ", "スポット", "宿", "快適さ"]:
            H.append(int(request.form[h]))
        m_item = AHP.matrix(H, 5)
        an = AHP.weight(m_item, 5)
        if D == "北海道・東北":
            Ha = [1, 2, 4, 3, 7, 5, 6, 8, 9, 11, 12, 10, 13]
        elif D == "関東":
            Ha = [13, 4, 2, 1, 9, 3, 5, 6, 7, 8, 11, 10, 12]
        elif D == "東海":
            Ha = [13, 10, 8, 5, 9, 2, 1, 3, 4, 6, 7, 11, 12]
        elif D == "近畿":
            Ha = [12, 9, 11, 8, 13, 6, 4, 2, 1, 3, 5, 7, 10]
        elif D == "中国・四国":
            Ha = [13, 10, 11, 9, 12, 7, 6, 5, 4, 2, 1, 3, 8]
        else:
            Ha = [11, 10, 13, 9, 12, 8, 7, 6, 5, 4, 3, 1, 2]
        if S >= 3 and S <= 5:#春
            #グルメ
            Hb = [11, 10, 2, 3, 12, 1, 5, 8, 9, 4, 7, 6, 13]
            #スポット
            Hc = [1, 9, 13, 11, 4, 12, 7, 6, 5, 10, 8, 2, 3]
            #宿
            Hd = [2, 5, 3, 1, 4, 7, 13, 8, 12, 11, 9, 10, 6]
            #快適さ
            He = [13, 12, 3, 2, 11, 1, 5, 6, 4, 7, 8, 9, 10]
        elif S >= 6 and S <= 8:#夏
            Hb = [2, 13, 10, 9, 11, 8, 12, 7, 3, 6, 5, 4, 1]
            Hc = [2, 8, 12, 10, 13, 11, 6, 5, 4, 9, 7, 3, 1]
            Hd = [2, 8, 9, 6, 7, 11, 12, 3, 13, 4, 5, 10, 1]
            He = [1, 2, 4, 5, 3, 6, 7, 13, 12, 10, 8, 11, 9]
        elif S >= 9 and S <= 11:#秋
            Hb = [2, 3, 9, 10, 5, 6, 11, 4, 12, 8, 1, 7, 13]
            Hc = [3, 4, 12, 10, 11, 8, 6, 1, 9, 7, 2, 5, 13]
            Hd = [1, 4, 8, 7, 3, 6, 12, 2, 13, 9, 5, 11, 10]
            He = [13, 11, 9, 10, 12, 1, 3, 8, 7, 6, 4, 5, 2]
        else:#冬
            Hb = [1, 4, 11, 12, 3, 5, 10, 8, 7, 9, 6, 2, 13]
            Hc = [1, 3, 4, 6, 2, 11, 12, 9, 5, 7, 8, 10, 13]
            Hd = [3, 4, 2, 5, 1, 6, 12, 7, 11, 10, 9, 8, 13]
            He = [12, 11, 10, 7, 13, 1, 4, 9, 8, 6, 5, 3, 2]
        #マトリックス作成
        ma = AHP.matrix(Ha, 13)
        mb = AHP.matrix(Hb, 13)
        mc = AHP.matrix(Hc, 13)
        md = AHP.matrix(Hd, 13)
        me = AHP.matrix(He, 13)
        #幾何平均による各案の評価値計算
        an_a = AHP.weight(ma, 13)
        an_b = AHP.weight(mb, 13)
        an_c = AHP.weight(mc, 13)
        an_d = AHP.weight(md, 13)
        an_e = AHP.weight(me, 13)

        result = [value for value in AHP.final(an, an_a, an_b, an_c, an_d, an_e)]
        result_list.append(result)
        return render_template("form4.html", S=S, D=D)
    else:
        return render_template("form3.html")
@app.route("/fourth", methods=["POST", "GET"])
def index3():
    if request.method == "POST":
        AHP = AHP_class()
        S = int(request.form["S"])
        D = request.form["D"]
        H = []
        for h in ["コスト", "グルメ", "スポット", "宿", "快適さ"]:
            H.append(int(request.form[h]))
        m_item = AHP.matrix(H, 5)
        an = AHP.weight(m_item, 5)
        if D == "北海道・東北":
            Ha = [1, 2, 4, 3, 7, 5, 6, 8, 9, 11, 12, 10, 13]
        elif D == "関東":
            Ha = [13, 4, 2, 1, 9, 3, 5, 6, 7, 8, 11, 10, 12]
        elif D == "東海":
            Ha = [13, 10, 8, 5, 9, 2, 1, 3, 4, 6, 7, 11, 12]
        elif D == "近畿":
            Ha = [12, 9, 11, 8, 13, 6, 4, 2, 1, 3, 5, 7, 10]
        elif D == "中国・四国":
            Ha = [13, 10, 11, 9, 12, 7, 6, 5, 4, 2, 1, 3, 8]
        else:
            Ha = [11, 10, 13, 9, 12, 8, 7, 6, 5, 4, 3, 1, 2]
        if S >= 3 and S <= 5:#春
            #グルメ
            Hb = [11, 10, 2, 3, 12, 1, 5, 8, 9, 4, 7, 6, 13]
            #スポット
            Hc = [1, 9, 13, 11, 4, 12, 7, 6, 5, 10, 8, 2, 3]
            #宿
            Hd = [2, 5, 3, 1, 4, 7, 13, 8, 12, 11, 9, 10, 6]
            #快適さ
            He = [13, 12, 3, 2, 11, 1, 5, 6, 4, 7, 8, 9, 10]
        elif S >= 6 and S <= 8:#夏
            Hb = [2, 13, 10, 9, 11, 8, 12, 7, 3, 6, 5, 4, 1]
            Hc = [2, 8, 12, 10, 13, 11, 6, 5, 4, 9, 7, 3, 1]
            Hd = [2, 8, 9, 6, 7, 11, 12, 3, 13, 4, 5, 10, 1]
            He = [1, 2, 4, 5, 3, 6, 7, 13, 12, 10, 8, 11, 9]
        elif S >= 9 and S <= 11:#秋
            Hb = [2, 3, 9, 10, 5, 6, 11, 4, 12, 8, 1, 7, 13]
            Hc = [3, 4, 12, 10, 11, 8, 6, 1, 9, 7, 2, 5, 13]
            Hd = [1, 4, 8, 7, 3, 6, 12, 2, 13, 9, 5, 11, 10]
            He = [13, 11, 9, 10, 12, 1, 3, 8, 7, 6, 4, 5, 2]
        else:#冬
            Hb = [1, 4, 11, 12, 3, 5, 10, 8, 7, 9, 6, 2, 13]
            Hc = [1, 3, 4, 6, 2, 11, 12, 9, 5, 7, 8, 10, 13]
            Hd = [3, 4, 2, 5, 1, 6, 12, 7, 11, 10, 9, 8, 13]
            He = [12, 11, 10, 7, 13, 1, 4, 9, 8, 6, 5, 3, 2]
        #マトリックス作成
        ma = AHP.matrix(Ha, 13)
        mb = AHP.matrix(Hb, 13)
        mc = AHP.matrix(Hc, 13)
        md = AHP.matrix(Hd, 13)
        me = AHP.matrix(He, 13)
        #幾何平均による各案の評価値計算
        an_a = AHP.weight(ma, 13)
        an_b = AHP.weight(mb, 13)
        an_c = AHP.weight(mc, 13)
        an_d = AHP.weight(md, 13)
        an_e = AHP.weight(me, 13)

        result = [value for value in AHP.final(an, an_a, an_b, an_c, an_d, an_e)]
        result_list.append(result)
        return render_template("form5.html", S=S, D=D)
    else:
        return render_template("form4.html")
@app.route("/fifth", methods=["POST", "GET"])
def index4():
    if request.method == "POST":
        AHP = AHP_class()
        S = int(request.form["S"])
        D = request.form["D"]
        H = []
        for h in ["コスト", "グルメ", "スポット", "宿", "快適さ"]:
            H.append(int(request.form[h]))
        m_item = AHP.matrix(H, 5)
        an = AHP.weight(m_item, 5)
        if D == "北海道・東北":
            Ha = [1, 2, 4, 3, 7, 5, 6, 8, 9, 11, 12, 10, 13]
        elif D == "関東":
            Ha = [13, 4, 2, 1, 9, 3, 5, 6, 7, 8, 11, 10, 12]
        elif D == "東海":
            Ha = [13, 10, 8, 5, 9, 2, 1, 3, 4, 6, 7, 11, 12]
        elif D == "近畿":
            Ha = [12, 9, 11, 8, 13, 6, 4, 2, 1, 3, 5, 7, 10]
        elif D == "中国・四国":
            Ha = [13, 10, 11, 9, 12, 7, 6, 5, 4, 2, 1, 3, 8]
        else:
            Ha = [11, 10, 13, 9, 12, 8, 7, 6, 5, 4, 3, 1, 2]
        if S >= 3 and S <= 5:#春
            #グルメ
            Hb = [11, 10, 2, 3, 12, 1, 5, 8, 9, 4, 7, 6, 13]
            #スポット
            Hc = [1, 9, 13, 11, 4, 12, 7, 6, 5, 10, 8, 2, 3]
            #宿
            Hd = [2, 5, 3, 1, 4, 7, 13, 8, 12, 11, 9, 10, 6]
            #快適さ
            He = [13, 12, 3, 2, 11, 1, 5, 6, 4, 7, 8, 9, 10]
        elif S >= 6 and S <= 8:#夏
            Hb = [2, 13, 10, 9, 11, 8, 12, 7, 3, 6, 5, 4, 1]
            Hc = [2, 8, 12, 10, 13, 11, 6, 5, 4, 9, 7, 3, 1]
            Hd = [2, 8, 9, 6, 7, 11, 12, 3, 13, 4, 5, 10, 1]
            He = [1, 2, 4, 5, 3, 6, 7, 13, 12, 10, 8, 11, 9]
        elif S >= 9 and S <= 11:#秋
            Hb = [2, 3, 9, 10, 5, 6, 11, 4, 12, 8, 1, 7, 13]
            Hc = [3, 4, 12, 10, 11, 8, 6, 1, 9, 7, 2, 5, 13]
            Hd = [1, 4, 8, 7, 3, 6, 12, 2, 13, 9, 5, 11, 10]
            He = [13, 11, 9, 10, 12, 1, 3, 8, 7, 6, 4, 5, 2]
        else:#冬
            Hb = [1, 4, 11, 12, 3, 5, 10, 8, 7, 9, 6, 2, 13]
            Hc = [1, 3, 4, 6, 2, 11, 12, 9, 5, 7, 8, 10, 13]
            Hd = [3, 4, 2, 5, 1, 6, 12, 7, 11, 10, 9, 8, 13]
            He = [12, 11, 10, 7, 13, 1, 4, 9, 8, 6, 5, 3, 2]
        #マトリックス作成
        ma = AHP.matrix(Ha, 13)
        mb = AHP.matrix(Hb, 13)
        mc = AHP.matrix(Hc, 13)
        md = AHP.matrix(Hd, 13)
        me = AHP.matrix(He, 13)
        #幾何平均による各案の評価値計算
        an_a = AHP.weight(ma, 13)
        an_b = AHP.weight(mb, 13)
        an_c = AHP.weight(mc, 13)
        an_d = AHP.weight(md, 13)
        an_e = AHP.weight(me, 13)

        result = [value for value in AHP.final(an, an_a, an_b, an_c, an_d, an_e)]
        result_list.append(result)
        return render_template("form6.html", S=S, D=D)
    else:
        return render_template("form5.html")
@app.route("/sixth", methods=["POST", "GET"])
def index5():
    if request.method == "POST":
        AHP = AHP_class()
        S = int(request.form["S"])
        D = request.form["D"]
        H = []
        for h in ["コスト", "グルメ", "スポット", "宿", "快適さ"]:
            H.append(int(request.form[h]))
        m_item = AHP.matrix(H, 5)
        an = AHP.weight(m_item, 5)
        if D == "北海道・東北":
            Ha = [1, 2, 4, 3, 7, 5, 6, 8, 9, 11, 12, 10, 13]
        elif D == "関東":
            Ha = [13, 4, 2, 1, 9, 3, 5, 6, 7, 8, 11, 10, 12]
        elif D == "東海":
            Ha = [13, 10, 8, 5, 9, 2, 1, 3, 4, 6, 7, 11, 12]
        elif D == "近畿":
            Ha = [12, 9, 11, 8, 13, 6, 4, 2, 1, 3, 5, 7, 10]
        elif D == "中国・四国":
            Ha = [13, 10, 11, 9, 12, 7, 6, 5, 4, 2, 1, 3, 8]
        else:
            Ha = [11, 10, 13, 9, 12, 8, 7, 6, 5, 4, 3, 1, 2]
        if S >= 3 and S <= 5:#春
            #グルメ
            Hb = [11, 10, 2, 3, 12, 1, 5, 8, 9, 4, 7, 6, 13]
            #スポット
            Hc = [1, 9, 13, 11, 4, 12, 7, 6, 5, 10, 8, 2, 3]
            #宿
            Hd = [2, 5, 3, 1, 4, 7, 13, 8, 12, 11, 9, 10, 6]
            #快適さ
            He = [13, 12, 3, 2, 11, 1, 5, 6, 4, 7, 8, 9, 10]
        elif S >= 6 and S <= 8:#夏
            Hb = [2, 13, 10, 9, 11, 8, 12, 7, 3, 6, 5, 4, 1]
            Hc = [2, 8, 12, 10, 13, 11, 6, 5, 4, 9, 7, 3, 1]
            Hd = [2, 8, 9, 6, 7, 11, 12, 3, 13, 4, 5, 10, 1]
            He = [1, 2, 4, 5, 3, 6, 7, 13, 12, 10, 8, 11, 9]
        elif S >= 9 and S <= 11:#秋
            Hb = [2, 3, 9, 10, 5, 6, 11, 4, 12, 8, 1, 7, 13]
            Hc = [3, 4, 12, 10, 11, 8, 6, 1, 9, 7, 2, 5, 13]
            Hd = [1, 4, 8, 7, 3, 6, 12, 2, 13, 9, 5, 11, 10]
            He = [13, 11, 9, 10, 12, 1, 3, 8, 7, 6, 4, 5, 2]
        else:#冬
            Hb = [1, 4, 11, 12, 3, 5, 10, 8, 7, 9, 6, 2, 13]
            Hc = [1, 3, 4, 6, 2, 11, 12, 9, 5, 7, 8, 10, 13]
            Hd = [3, 4, 2, 5, 1, 6, 12, 7, 11, 10, 9, 8, 13]
            He = [12, 11, 10, 7, 13, 1, 4, 9, 8, 6, 5, 3, 2]
        #マトリックス作成
        ma = AHP.matrix(Ha, 13)
        mb = AHP.matrix(Hb, 13)
        mc = AHP.matrix(Hc, 13)
        md = AHP.matrix(Hd, 13)
        me = AHP.matrix(He, 13)
        #幾何平均による各案の評価値計算
        an_a = AHP.weight(ma, 13)
        an_b = AHP.weight(mb, 13)
        an_c = AHP.weight(mc, 13)
        an_d = AHP.weight(md, 13)
        an_e = AHP.weight(me, 13)

        result = [value for value in AHP.final(an, an_a, an_b, an_c, an_d, an_e)]
        result_list.append(result)
        r_list = [1.4, 1.2, 0.8, 0.8, 0.8]
        item2 = {"北海道":"hokkaido", "宮城":"miyagi", "栃木":"tochigi", "横浜":"yokohama", "新潟":"niigata", "静岡":"shizuoka", "名古屋":"nagoya", "京都":"kyoto", "大阪":"osaka", "神戸":"kobe", "広島":"hiroshima", "博多":"hakata", "沖縄":"okinawa"}
        res_d = []
        for result_l, r in zip(result_list, r_list):
            res_d.append(list(map(lambda q : q*r, result_l)))
        result_d = [sum(x) for x in zip(*res_d)]
        result_dict = {it : r_d for it, r_d in zip(item2, result_d)}
        Result = sorted(result_dict.items(), key=lambda x:x[1], reverse=True)
        result1 = Result[0][0]
        link1 = "https://travel.rakuten.co.jp/mytrip/ranking/spot-"+item2[result1]
        result2 = Result[1][0]
        link2 = "https://travel.rakuten.co.jp/mytrip/ranking/spot-"+item2[result2]
        result3 = Result[2][0]
        link3 = "https://travel.rakuten.co.jp/mytrip/ranking/spot-"+item2[result3]
        others = []
        for i in range(3, 13):
            others.append(Result[i][0])
        return render_template("result.html", S=S, D=D, result1=result1, result2=result2, result3=result3, link1=link1, link2=link2, link3=link3, others=others)
    else:
        return render_template("form6.html")


if __name__ == "__main__":
    app.run(debug=True)
