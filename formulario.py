
class Categoria(models.Model):

    Nome_da_categoria = models.CharField(max_length=100)

    def __str__(self):

       return self.Nome_da_categoria

    Ativada = models.BooleanField()
    Obs_da_categoria = models.TextField()
    Data_de_cadastro_da_categoria = models.DateField()

class Cliente(models.Model):

    Categoria_do_cliente = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Cliente_ativo = models.BooleanField()
    Nome_fantasia = models.CharField(max_length=100)

    def __str__(self):

       return self.Nome_fantasia

    Nome_do_cliente = models.CharField(max_length=100)
    Razao_social = models.CharField(max_length=100)
    #Logo_do_cliente = models.ImageField(upload_to=’upload/’)
    Site_do_cliente = models.URLField()

    TIPOJURIDICODOCLIENTE = {

           (“MEI”, “Microempreendedor Individual”),
           (“PF”, “Pessoa Física”),
           (“CS”, “Simples”),

    }

    Tipo_juridico_do_cliente = models.CharField(max_length=50, choices=TIPOJURIDICODOCLIENTE)
    Cnpj = models.CharField(max_length=100)
    Inscricao_estadual = models.CharField(max_length=50)

    RESPOSTACONTRATO = {

        (“SC”, “Sem contrato”),
        (“EN”, “Contrato em negociação”),
        (“CC”, “Possui contrato”),
    }


    Possui_contrato = models.CharField(max_length=30, choices=RESPOSTACONTRATO)
   # Contrato_anexado = models.FileField(upload_to=’upload/’)
    Valor_total_do_contrato = models.FloatField()