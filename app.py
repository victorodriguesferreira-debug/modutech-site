from flask import Flask, render_template, request, redirect
from urllib.parse import quote
app = Flask(__name__)
PHONE='5511940030056'
SERVICES=[('Chaveiro automotivo','Chaves codificadas, chips, controles, abertura e imobilizadores.','🔑'),('Módulos eletrônicos','Venda, instalação, reparo e programação de módulos.','🧠'),('Autoelétrica','Diagnósticos, sensores, chicotes e sistemas elétricos.','⚡'),('Remap e performance','Encaminhamento a especialistas em reprogramação.','🏁'),('Som e acessórios','Multimídia, alto-falantes, câmeras e acessórios.','🔊'),('Mecânica geral','Avaliação e encaminhamento a oficinas parceiras.','🔧')]
@app.route('/')
def index(): return render_template('index.html',services=SERVICES)
@app.route('/solicitar',methods=['POST'])
def solicitar():
    f=request.form
    fields=[('Nome',f.get('nome','')),('Telefone',f.get('telefone','')),('Serviço',f.get('servico','')),('Veículo',f.get('veiculo','')),('Ano',f.get('ano','')),('Localização',f.get('local','')),('Urgência',f.get('urgencia','')),('Descrição',f.get('descricao',''))]
    msg='Olá, ModuTech! Preciso de atendimento.\n'+'\n'.join(f'{k}: {v}' for k,v in fields if v.strip())
    return redirect('https://wa.me/'+PHONE+'?text='+quote(msg))
if __name__=='__main__': app.run(debug=True)
