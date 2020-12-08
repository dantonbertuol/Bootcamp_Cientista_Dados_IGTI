-- Questão 01 - Respota 5
SELECT COUNT(*) FROM estado WHERE NomeEstado like 'P%';

-- Questão 02 - Resposta 13
SELECT COUNT(*) FROM CARACTERISTICASGERAIS ;

-- Questão 03 - Resposta 8
SELECT COUNT(*) FROM IMOVEL IMO
INNER JOIN CIDADE CID ON CID.CODIGOCOMPLETOIBGE  = IMO.CODIGOCOMPLETOIBGE
INNER JOIN ESTADO EST ON EST.CODESTADOIBGE  = CID.CODESTADOIBGE
WHERE EST.SIGLAESTADO = 'RS';

-- Questão 11 - Resposta 7
SELECT COUNT(DISTINCT EST.NOMEESTADO) AS QTD_ESTADOS FROM IMOVEL IMO
INNER JOIN CIDADE CID ON CID.CODIGOCOMPLETOIBGE  = IMO.CODIGOCOMPLETOIBGE
INNER JOIN ESTADO EST ON EST.CODESTADOIBGE  = CID.CODESTADOIBGE
WHERE IMO.VALORCONDOMINIO  = 0 ;

-- Questão 12 - Resposta 104 (Valor aproximado no trabalho e 103)
SELECT COUNT(*) FROM CARACTERISTICAGERALIMOVEL ;

-- Questão 13 - Resposta 8004320000000
SELECT IMO.CODREGISTRO FROM IMOVEL IMO
ORDER BY IMO.VALORCONDOMINIO DESC
LIMIT 1;