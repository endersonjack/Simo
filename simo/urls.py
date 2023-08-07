from engenharia.views import *
from simo.utils import limpar_cache
from tarefas.views import *
import debug_toolbar
from recibos.views import *
from simo.settings import STATIC_URL
from funcionarios.views import *
from estoque.views import *
from requisicao.views import *
from financeiro.views import *
from financeiro.validations import *
from servicos.views import *
from dashboard.views import *
from obras.views import *
from faturamento.views import *
from fornecedores.views import *
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from financeiro.ajax import *

# handler404 = 'simo.utils.handler404'   


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path("select2/", include("django_select2.urls")),
    
    #url DashBoard
    path('', home_index, name='dashboard'),
    path('tarefa/novo', criar_tarefas, name='criar-tarefa'),
    path('tarefa/criar', salvar_tarefa, name='salvar-tarefa'),
    path('tarefa/editar/salvar/<int:pk>', salvar_edicao_tarefa, name='salvar-edicao-tarefa'),
    path('tarefa/<int:pk>', ver_tarefa, name='ver-tarefa'),
    path('tarefa/<int:pk>/detalhes', ver_tarefa_detalhes, name='ver-tarefa-detalhes'),
    path('tarefa/excluir/<int:pk>', excluir_tarefa, name='excluir-tarefa'),
    path('tarefa/editar/<pk>', editar_tarefa, name='editar-tarefa'),
    path('tarefa/realizar/<pk>', marcar_realizar_tarefa, name='realizar-tarefa'),

   
    #urls Estoque
    path('ver-estoque', InicioEstoque.as_view(), name='ver-estoque'),
    path('ver-estoque/varios', VerEstoqueVarios.as_view(), name='ver-estoque-varios'),
    path('add-varios/', add_filtro_varios, name='add-varios'),
    path('remover-item-selecionado/', remover_filtro_varios, name='remover-item-selecionado'),
    path('remover-lista-selecionada/', remover_lista_selecionada, name='remover-lista-selecionada'),
    path('mov-estoque/', MovimentacaoEstoqueView.as_view(), name='mov-estoque'),
    path('buscar-estoque/', BuscaEstoqueView.as_view(), name='buscar-estoque'),
    path('categorias-estoque/', CategoriasEstoque.as_view(), name='categorias-estoque'),
    path('categorias-estoque/editar/<pk>', EditarCategoriaEstoque.as_view(), name='editar-categoria'),
    path('categorias-estoque/excluir/<pk>', ExcluirCategoriaEstoque.as_view(), name='excluir-categoria'),
    path('inserir-item/', InserirItemView.as_view(), name='inserir-item'),
    path('excluir-item/<pk>', ExcluirItemView.as_view(), name='excluir-item'),
    path('detalhar-item/<pk>', DetalharItemView.as_view(), name='detalhar-item'),
    path('editar-item/<pk>', EditarItemView.as_view(), name='editar-item'),
    path('imprimir-resultados', ImprimirResultadosEstoqueView.as_view(), name='imprimir-resultados'),
    path('imprimir-lista-itens', ImprimirListaItensView.as_view(), name='imprimir-lista-itens'),
    path('filtrar-estoque', estoque_filter, name='estoque-filter'),
    
    #urls Requisição
    path('gerar-requisicao/', GerarRequisicaoView.as_view(), name='gerar-requisicao'),
    path('imprimir-requisicao/<int:pk>', imprimir_requisicao, name='imprimir-requisicao'),
    path('requisicoes/geradas', ver_requisicoes, name='ver-requisicoes'),
    path('requisicoes/itens-requisicao/<int:pk>', ver_itens_requisicao, name='ver-itens-requisicao'),


    #urls Obras
    path('inserir-obra/', InserirObraView.as_view(), name='inserir-obra'),
    path('ver-obras/', BuscarObraListView.as_view(), name='ver-obras'),
    path('local/inserir', inserir_local, name='inserir-local'),
    path('local/<int:pk>/excluir', excluir_local, name='excluir_local'),
    path('local/<int:pk>/editar', editar_local, name='editar_local'),
    path('hx/get_locais', get_locais, name='get_locais'),
    

    #urls Serviços
    path('os/', OrdemServicoCreateView.as_view(), name='inserir-ordem'),
    path('os/<pk>/excluir-ordem', ExcluirOrdemDeServicoView.as_view(), name='excluir-ordem'),
    path('os/<pk>/inserir-servico', ServicoCreateView.as_view(), name='inserir-servico'),
    path('os/<id_ordem>/<pk>/editar-servico', EditarServicoView.as_view(), name='editar-servico'), #VIEWS GENERICAS COMO UPDATEVIEW reservam o 'pk' para a id do objeto
    path('os/<id_ordem>/<pk>/excluir-servico', ExcluirServicoView.as_view(), name='excluir-servico'),
    path('os/<id_ordem>/<pk>/detalhar-servico', DetalharServicoView.as_view(), name='detalhar-servico'),
    path('os/<id_ordem>/<pk>/finalizar-servico', FinalizarServicoView.as_view(), name='finalizar-servico'),
    path('os/<id_ordem>/<pk>/imprimir-servico', ImprimirServicoView.as_view(), name='imprimir-os-servico'),
    path('os/<id_ordem>/<pk>/inserir-funcionario', InserirFuncionarioServicoView.as_view(), { 'editar': False }, name='inserir-funcionario-servico'),
    path('os/<id_ordem>/<pk>/editar-funcionario', InserirFuncionarioServicoView.as_view(), { 'editar': True }, name='editar-funcionario-servico'),
    path('os/<id_ordem>/<pk>/inserir-itens', ItensServicoCreateView.as_view(), name='inserir-itens-servico'),
    path('salvar-ordem-servico/os/<pk>', SalvarServicoView.as_view(), name='salvar-ordem-servico'),
    path('listar-servicos/', ListServicosView.as_view(), name='listar-servicos'),
    path('listar-servicos-funcionario/', ListFuncionarioServicosView.as_view(), name='listar-servicos-funcionario'),
    path('listar-ordens/', ListOrdensView.as_view(), name='listar-ordens'),
    path('anexar-imagens-servicos/os/<pk>/servico/<int:idServ>', AnexarImagensServicoView.as_view(), name='anexar-imagens-servicos'),
    path('deletar-imagem/os/<id_ordem>/servico/<idServ>/deletar-imagem/<pk>', DeletarImagemServicoView.as_view(), name='deletar-imagem'),
    path('imprimir-servicos/', ImprimirListaServicosView.as_view(), name='imprimir-servicos'),
    path('imprimir-servicos-funcionario/', ImprimirListaFuncionarioServicosView.as_view(), name='imprimir-servicos-funcionario'),

    #auto-completes
    path('autocomplete-funcionarios/', autocompletefuncionario, name='autocomplete-funcionarios'),
#    path('gerar-requisicao/busca_funcionarios', autocomplete_funcionarios, name='autocomplete-funcionarios-requisicao'),
    path('autocomplete-itens/', autocompleteitens, name='autocomplete-itens'),
    
    #urls Usuários 
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    
    #urls Financeiro 
    path('resumo-do-dia/', home_resumo_do_dia, name='resumo-do-dia'),
    path('contas-a-pagar/', contas_a_pagar, name='contas-a-pagar'),
    path('contas-atrasadas/', contas_atrasadas, name='contas-atrasadas'),
    path('contas-a-pagar/filtro', filtro_contas_a_pagar, name='resultados-filtro-contas-a-pagar'),
    path('contas-a-pagar/add-descricao', add_descricao_nota, name='add-descricao-nota'),          
    path('contas-a-pagar/inserir', inserir_nova_conta_a_pagar, name='inserir-conta-a-pagar'),
    path('contas-a-pagar/modal-itens/', modal_itens_conta_a_pagar, name='modal-item-conta'),
    path('contas-a-pagar/modal-itens/<int:pk>', modal_itens_conta_a_pagar, name='modal-item-conta'),
    path('contas-a-pagar/inserir-itens/', inserir_itens_conta_a_pagar, name='inserir-itens-conta'),
    path('contas-a-pagar/inserir-itens/<int:pk>', inserir_itens_conta_a_pagar, name='inserir-itens-conta'),
    path('contas-a-pagar/excluir-item/<int:pk>', excluir_item_conta_a_pagar, name='excluir-item-conta'),

    #VALIDAÇÕES E BUSCAS Engenharia v.2
    path('hx/validar/numero_os', hx_verificar_numero_os, name='hx_verificar_numero_os'),
    path('hx/obra/<int:pk>/filter_ordens', hx_filtrar_os, name='hx_filtrar_os'),
    
    #urls Engenharia v.2
    path('engenharia/', home_engenharia, name='home_engenharia'),
    path('engenharia/obra/<int:pk>/os', home_obras_ver_servicos, name='home_obra_os'),
    path('engenharia/obra/<int:pk>/todas_os', ver_todas_os_por_obra, name='ver_todas_os_por_obra'),
    path('engenharia/obra/<int:pk>/nova_os', obras_nova_orden_servico, name='obra_nova_os'),
    path('engenharia/obra/<int:pk>/nova_os/salvar', obras_salvar_nova_orden_servico, name='obra_salvar_nova_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/editar', obras_editar_orden_servico, name='obra_editar_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/salvar', obras_salvar_editar_orden_servico, name='obra_salvar_editar_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar', obras_detalhar_orden_servico, name='obra_detalhar_os'),
    #urls Engenharia Imagens v.2
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens', obras_imagens_orden_servico, name='obra_imagens_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/inserir_categoria', obras_imagens_inserir_categoria_orden_servico, name='obra_imagens_inserir_categoria_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/categoria/<int:cat>/editar_categoria', obras_editar_categoria_orden_servico, name='obra_editar_categoria'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/categoria/<int:cat>/excluir_categoria', obras_excluir_categoria_orden_servico, name='obra_excluir_categoria'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/salvar_categoria', obras_imagens_salvar_categoria_orden_servico, name='obra_imagens_salvar_categoria_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/inserir_imagem', obras_inserir_imagem_em_categoria_orden_servico, name='inserir_imagem_em_categoria'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/salvar_imagem', obras_salvar_imagem_em_categoria_orden_servico, name='salvar_imagem_em_categoria'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/<int:im>/excluir_imagem', obras_excluir_imagem_orden_servico, name='excluir_imagem_em_categoria'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/<int:im>/editar_categoria_imagem', obras_editar_categoria_imagem_orden_servico, name='editar_categoria_imagem'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/imagens/categoria/<int:cat>/download_imagens_por_categoria', dowload_imagens_categoria_orden_servico, name='dowload_imagens_categoria'),
    #urls Engenharia Documentos v.2
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/documentos', documentos_orden_servico, name='documentos_orden_servico'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/documentos/salvar', salvar_documento_os, name='salvar_documento_os'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/documentos/<int:file>/excluir', excluir_arquivo_os, name='excluir_arquivo_os'),
    #urls Engenharia RDO v.2
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/diariodeobra', rdo_orden_servico, name='rdo_orden_servico'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/diariodeobra/salvar', salvar_rdo_orden_servico, name='salvar_rdo_orden_servico'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/diariodeobra/<int:rdo>/editar', editar_rdo_orden_servico, name='editar_rdo_orden_servico'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/diariodeobra/<int:rdo>/salvar', salvar_editar_rdo_orden_servico, name='salvar_editar_rdo_orden_servico'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/diariodeobra/<int:rdo>/detalhar', detalhar_rdo_rdo_orden_servico, name='detalhar_rdo_rdo_orden_servico'),
    path('engenharia/obra/<int:pk>/os/<int:os>/detalhar/diariodeobra/<int:rdo>/excluir', excluir_rdo_orden_servico, name='excluir_rdo_orden_servico'),

    
    
    
    #urls Financeiro v.2
    path('contas-a-pagar/salvar-saida', salvar_nota_completa, name='salvar-saida'),
    path('contas-a-pagar/nota/<int:pk>', ver_nota_completa, name='ver-nota-completa'),
    path('contas-a-pagar/editar/saida/<int:pk>', editar_saida, name='editar-saida'),
    path('contas-a-pagar/editar/saida/salvar/<int:pk>', salva_edicao_saida, name='salvar-edicao-saida'),
    path('contas-a-pagar/excluir/saida/<int:pk>', excluir_saida, name='excluir-saida'),
    path('contas-a-pagar/forma-pagamento/<int:pk>', selecionar_forma_de_pagamento, name='modal-ver-formas-pagamentos'),
    path('contas-a-pagar/forma-pagamento-selecionada/<int:pk>', forma_de_pagamento_selecionada, name='forma-pagamento-selecionada'),
    path('contas-a-pagar/get-valor-total', get_valor_total, name='get-valor-total'),
    path('contas-a-pagar/pagar/nota/<int:pk>', pagar_nota_a_vista, name='pagar-conta-vista'),
    path('contas-a-pagar/excluir-pagamento-vista/nota/<int:pk>', excluir_pagamento_a_vista, name='excluir-pagamento-vista'),
    path('contas-a-pagar/<int:pk>/get-resumo-boleto-mensal', get_resumo_boleto_mensal, name='resumo-boleto-mensal'),
    path('contas-a-pagar/<int:pk>/atualizar-resumo-boleto-mensal', atualizar_resumo_boleto_mensal, name='atualizar-resumo-boleto-mensal'),
    path('contas-a-pagar/<int:pk>/salvar-boletos-mensal', salvar_boletos_mensal, name='salvar-boletos-mensal'),
    path('contas-a-pagar/excluir-pagamento-boletos/nota/<int:pk>', excluir_pagamento_boletos, name='excluir-pagamento-boletos'),
    path('contas-a-pagar/editar-pagamento-boletos/nota/<int:pk>', editar_pagamento_boletos, name='editar-pagamento-boletos'),
    path('contas-a-pagar/editar-pagamento-vista/nota/<int:pk>', editar_pagamento_vista, name='editar-pagamento-vista'),
    path('contas-a-pagar/salvar-editar-pagamento-vista/<int:pk>/nota/<int:nota>', salvar_editar_pagamento_vista, name='salvar-edicao-pagamento-vista'),
    path('contas-a-pagar/editar-pagamento-boleto/<int:pk>/nota/<int:nota>', editar_pagamento_boleto, name='editar-pagamento-boleto'),
    path('contas-a-pagar/salvar-editar-boleto/<int:pk>/nota/<int:nota>', salvar_editar_pagamento_boleto, name='salvar-editar-boleto-unico'),
    path('contas-a-pagar/excluir-boleto-unico/<int:pk>/nota/<int:nota>', excluir_boleto_unico, name='excluir-boleto-unico'),
    path('contas-a-pagar/pagar-boleto-unico/<int:pk>/nota/<int:nota>', pagar_boleto_unico, name='pagar-boleto-unico'),
    path('contas-a-pagar/salvar-pagar-boleto-unico/<int:pk>/nota/<int:nota>', salvar_pagar_boleto_unico, name='salvar-pagamento-boleto-unico'),
    path('contas-a-pagar/excluir-pagamento-boleto-unico/<int:pk>/nota/<int:nota>', excluir_pagamento_boleto_unico, name='excluir-pagamento-boleto-unico'),
    
    #inserir_nota_saida
    path('contas-a-pagar/inserir-descricao-saida', inserir_descricao_saida, name='inserir-descricao-saida'),
    path('contas-a-pagar/editar-descricao-saida/<int:pk>/nota/<int:nota>', editar_descricao_saida, name='editar-descricao-saida'),
    path('contas-a-pagar/salvar-descricao-saida', salvar_descricao_saida, name='salvar-descricao-saida'),
    path('contas-a-pagar/salvar-editar-descricao-saida/<int:pk>/nota/<int:nota>', salvar_editar_descricao_saida, name='salvar-editar-descricao-saida'),
    path('contas-a-pagar/inserir-itens-saida/nota/<int:pk>', inserir_itens_saida, name='inserir-itens-saida'),
    path('contas-a-pagar/salvar-itens-saida/nota/<int:pk>', salvar_itens_saida, name='salvar-itens-saida'),
    path('contas-a-pagar/salvar-itens-saida/<int:pk>/nota/<int:nota>', excluir_iten_saida, name='excluir-iten-saida'),
    
    #validações [financeiro]
    path('contas-a-pagar/check-descricao-item-conta', check_descricao_item_conta, name='check-descricao-item-conta'),
    path('contas-a-pagar/check-quantidade-item-conta', check_quantidade_item_conta, name='check-quantidade-item-conta'),
    path('contas-a-pagar/check-valor-item-conta', check_valor_item_conta, name='check-valor-item-conta'),
    path('contas-a-pagar/check-data-emissao', check_data_emissao, name='check-data-emissao'),
    path('contas-a-pagar/check-centro-de-custo', check_centro_de_custo, name='check-centro-de-custo'),
    path('contas-a-pagar/check-qtd-itens-conta', check_qtd_itens_conta, name='check-qtd-itens-conta'),
    
    
    
    # path('contas-a-pagar/editar/<pk>', EditarContasAPagarView.as_view(), name='editar-conta-a-pagar'),
    # path('contas-a-pagar/excluir/<pk>', ExcluirContasAPagarView.as_view(), name='excluir-conta-a-pagar'),
    # path('pagamento/<pk>', PagamentoView.as_view(), name='pagar-conta'),
    # path('pagamento/editar/<pk>', EditarPagamentoView.as_view(), name='editar-pagamento'),
    # path('pagamento/excluir/<pk>', ExcluirPagamentoView.as_view(), name='excluir-pagamento'),
    # path('relatorios/financeiro/contas-a-pagar', RelatoriosCostasAPagarView.as_view(), name='relatorios-contas-a-pagar'),
    # path('relatorio-contas/imprimir', ImprimirRelatoriosCostasAPagarView.as_view(), name='imprimir-relatorio-contas'),
    # path('contas-a-receber/', ContasAReceberView.as_view(), name='contas-a-receber'),
    # path('contas-a-receber/editar/<pk>', EditarRecebimentoView.as_view(), name='editar-conta-a-receber'),
    # path('contas-a-receber/excluir/<pk>', ExcluirRecebimentoView.as_view(), name='excluir-conta-a-receber'),
    path('recibos/', InserirReciboFornecedorView.as_view(), name='inserir-recibo'),
    path('recibos/editar/<pk>', EditarReciboFornecedorView.as_view(), name='editar-recibo'),
    path('recibos/excluir/<pk>', ExcluirReciboFornecedorView.as_view(), name='excluir-recibo'),
    path('recibos/imprimir/<pk>',ImprimirReciboFornecedorView.as_view(), name='imprimir-recibo'),
    # path('contas-pagas/', ContasPagasView.as_view(), name='contas-pagas'),
    # path('ajax/fornecedor/contas-a-pagar', getContasAPagar, name = "ajax-fornecedor-contas-a-pagar"),

    
    #urls Fornecedores
     path('fornecedores/', ListarFornecedorView.as_view(), name='listar-fornecedores'),
     path('fornecedor/<pk>', DetalharFornecedorView.as_view(), name='detalhar-fornecedor'),
     path('fornecedores/inserir', InserirFornecedorView.as_view(), name='inserir-fornecedor'),
     path('fornecedores/<pk>/editar', EditarFornecedorView.as_view(), name='editar-fornecedor'),
     path('fornecedores/<pk>/excluir', ExcluirFornecedorView.as_view(), name='excluir-fornecedor'),
     
     
    path('fornecedores/get', get_fornecedores, name='get-fornecedores'),
    path('fornecedores/get/error', get_error, name='get-error'),
    

    #urls Funcionários
     path('funcionarios/', InserirFuncionarioView.as_view(), name='inserir-funcionario'),
     path('funcionarios/<pk>/editar', EditarFuncionarioView.as_view(), name='editar-funcionario'),
     path('funcionarios/<pk>/excluir', ExcluirFuncionarioView.as_view(), name='excluir-funcionario'),
     path('funcionario/<pk>', DetalharFuncionarioView.as_view(), name='detalhar-funcionario'),
     path('cargos/', InserirCargoView.as_view(), name='inserir-cargo'),
     path('cargos/<pk>/editar', EditarCargoView.as_view(), name='editar-cargo'),
     path('cargos/<pk>/excluir', ExcluirCargoView.as_view(), name='excluir-cargo'),
     path('cargo/<pk>', DetalharCargoView.as_view(), name='detalhar-cargo'),

      #urls Faturamento
     path('faturamentos/', FaturamentoView.as_view(), name='listar-faturamentos'),
     path('faturamentos/inserir', InserirFaturamentoView.as_view(), name='inserir-faturamento'),
     path('faturamentos/editar/<pk>', EditarFaturamentoView.as_view(), name='editar-faturamento'),
     path('faturamentos/excluir/<pk>', ExcluirFaturamentoView.as_view(), name='excluir-faturamento'),
     path('faturamentos/imprimir', ImprimirFaturamentoView.as_view(), name='imprimir-faturamento'),
]

htmlx_urlpatterns = [     
    #REQUISIÇÕES         
    path('requisicao/requerente', requisicao_search_funcionario, name='requisicao-search-funcionario'),                 
    path('requisicao/add-requerente/<pk>', requisicao_add_funcionario, name='requisicao-add-funcionario'),                 
    path('requisicao/add-obra', requisicao_add_obra, name='requisicao-add-obra'),                 
    path('requisicao/add-local', requisicao_add_local, name='requisicao-add-local'),                 
    path('requisicao/add-itens-selecionados/<pk>', requisicao_add_itens_selecionados, name='requisicao-add-itens-selecionados'),                 
    path('requisicao/excluir-itens-selecionados/<pk>', requisicao_excluir_item_lista_selecionada, name='excluir-item-lista-selecionada'),                 
    path('hx/limpar-itens_lista', limpar_itens_lista, name='limpar-lista-itens'),                 
    path('hx/limpar-itens_selecionados', limpar_itens_selecionados, name='limpar-itens'),                 
    path('hx/limpar-tudo-requisicao', limpar_tudo_requisicao, name='limpar-tudo-requisicao'),                 
    path('requisicao/verificar-qnt/<int:pk>', requisicao_verificar_qnt, name='requisicao-verificar-qnt'),                 
    path('requisicao/salvar', requisicao_salvar, name='salvar-requisicao'),                 
    path('estoque/busca-varios', estoque_busca_varios, name='buscar-estoque-varios'),
    path('requisicao/buscar', buscar_requisicoes, name='buscar-requisicoes'),
    path('requisicao/excluir/<int:pk>', excluir_requisicoes, name='excluir-requisicao'),
    
    #utils
    path('hx/limpar', limpar_cache, name='limpar-cache'),                

]

urlpatterns += htmlx_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

     