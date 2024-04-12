from abc import ABC,abstractclassmethod,
abstractproperty
from datetime import datetime

class Cliente:
  def __init__(self,endereco):
    self.endereco = endereco
    self.contas = []
  
  def realizarTransicao(self,conta,transacao):
    transacao.registrar(conta)

  def adicionarConta(self,conta):
    self.contas.append(conta)

class PessoaFisica(Cliente):

class Conta:
  def __init__(self,numero,cliente):
    self._saldo = 0
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._historico = Historico()
class ContaCorrente(Conta):

class Historico:

class 
  