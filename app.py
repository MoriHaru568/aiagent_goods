import os

# Chroma の設定を先に
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"
os.environ["CHROMA_PERSIST_DIRECTORY"] = "/tmp/chroma"

# 必要であればディレクトリ作成
os.makedirs("/tmp/chroma", exist_ok=True)

from flask import Flask, render_template, request
from langchain.chat_models import ChatOpenAI
from utils.makeAgent import makeAgent
from utils.makeTask import makeTask
from utils.makeCrew import makeCrew

app = Flask(__name__)

# フォーム画面
@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

# フォーム送信後の処理更新
@app.route('/generate', methods=['POST'])
def generate():
    genre = request.form['genre']
    features = request.form['features']
    target = request.form['target']

    product_info = f"・商品ジャンル：{genre}\n・特徴：{features}\n・ターゲット層：{target}"

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7,max_completion_tokens=500)

    # Agents
    market = makeAgent("市場調査員", "ターゲットのニーズを分析", "美容業界専門家", llm)
    competitor = makeAgent("競合分析官", "競合商品を調査", "ブランド分析が得意", llm)
    namer = makeAgent("ネーミング担当", "商品名を考案", "コピー戦略の達人", llm)
    copywriter = makeAgent("コピーライター", "キャッチコピーを考案", "SNS向け表現のプロ", llm)

    # Tasks
    task1 = makeTask(f"{product_info} に対して市場分析を行ってください", "市場レポート", market)
    task2 = makeTask(f"{product_info} に関連する競合商品を調査し、差別化点を明確にしてください", "競合分析", competitor)
    task3 = makeTask(f"{product_info}\n[市場＆競合分析に基づき] 魅力的な商品名を3案考案してください", "商品名案", namer)
    task4 = makeTask(f"{product_info}\n[すべての情報をもとに] 印象的なキャッチコピーを3案考えてください", "キャッチコピー案", copywriter)

    crew = makeCrew([market, competitor, namer, copywriter], [task1, task2, task3, task4])
    result = crew.kickoff()

    market_report = result.tasks_output[0].raw
    competitive_analysis = result.tasks_output[1].raw
    goodsname_idea = result.tasks_output[2].raw
    catchphrase_idea = result.tasks_output[3].raw

    return render_template('result.html', market_report=market_report,competitive_analysis=competitive_analysis,goodsname_idea=goodsname_idea,catchphrase_idea=catchphrase_idea)

if __name__ == '__main__':
    app.run(debug=True)
