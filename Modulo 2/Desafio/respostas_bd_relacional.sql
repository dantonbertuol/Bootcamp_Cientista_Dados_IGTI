#Pergunta 1 - Resposta: 30
 SELECT
	count(*)
FROM
	TB_PESSOA
WHERE
	IDADE >= 50;

#Pergunta 2 - Resposta: 44.6
 SELECT
	avg(idade)
FROM
	TB_PESSOA PES
INNER JOIN TB_CIDADE CID ON
	CID.ID = PES.ID_CIDADE
INNER JOIN TB_ESTADO EST ON
	EST.ID = CID.ID_ESTADO
WHERE
	EST.SIGLA = 'MT';

#Pergunta 3 - Resposta: 14
 SELECT
	COUNT(*)
FROM
	TB_PESSOA PES
WHERE
	YEAR (PES.DATA_NASC) BETWEEN 1968 AND 1978;

#Pergunta 4 - Resposta: 4
 SELECT
	count(*)
FROM
	tb_pessoa
INNER JOIN tb_tiposanguineo ON
	tb_pessoa.id_tiposanguineo = tb_tiposanguineo.id
INNER JOIN tb_cidade ON
	tb_pessoa.id_cidade = tb_cidade.id
INNER JOIN tb_estado ON
	tb_cidade.id_estado = tb_estado.id
WHERE
	tb_tiposanguineo.tipo LIKE "AB-"
	AND (tb_estado.sigla LIKE "AP"
	OR tb_estado.sigla LIKE "PE");

#Pergunta 5 - Resposta: Thales Bento
 SELECT
	*
FROM
	TB_PESSOA PES
ORDER BY
	PES.IDADE DESC
LIMIT 1;

#Pergunta 6 - Resposta: João Pedro
 SELECT
	*
FROM
	TB_PESSOA PES
ORDER BY
	PES.IDADE ASC
LIMIT 1;
