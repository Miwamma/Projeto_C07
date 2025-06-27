CREATE DATABASE IF NOT EXISTS projetobd;
USE projetobd;

CREATE TABLE IF NOT EXISTS Log (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    acao VARCHAR(20),
    descricao TEXT,
    data_log TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Marca (
    id_marca INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Carro (
    id_carro INT PRIMARY KEY AUTO_INCREMENT,
    id_marca INT,
    nome VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_marca) REFERENCES Marca(id_marca)
);

CREATE TABLE IF NOT EXISTS Piloto (
    id_piloto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Carro_Piloto (
    id_carro INT,
    id_piloto INT,
    PRIMARY KEY (id_carro, id_piloto),
    FOREIGN KEY (id_carro) REFERENCES Carro(id_carro),
    FOREIGN KEY (id_piloto) REFERENCES Piloto(id_piloto)
);

CREATE TABLE IF NOT EXISTS Equipamento_Seguranca (
    id_equipamento INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Piloto_Equipamento (
    id_piloto INT,
    id_equipamento INT,
    PRIMARY KEY (id_piloto, id_equipamento),
    FOREIGN KEY (id_piloto) REFERENCES Piloto(id_piloto),
    FOREIGN KEY (id_equipamento) REFERENCES Equipamento_Seguranca(id_equipamento)
);

CREATE TABLE IF NOT EXISTS Patrocinador (
    id_patrocinador INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Marca_Patrocinador (
    id_marca INT,
    id_patrocinador INT,
    PRIMARY KEY (id_marca, id_patrocinador),
    FOREIGN KEY (id_marca) REFERENCES Marca(id_marca),
    FOREIGN KEY (id_patrocinador) REFERENCES Patrocinador(id_patrocinador)
);

-- Atualizações
UPDATE Carro SET nome = 'Carro Atualizado' WHERE id_carro = 1;

UPDATE Piloto SET nome = 'Piloto Atualizado' WHERE id_piloto = 1;

-- Excluindo
DELETE FROM Carro_piloto WHERE id_carro = 2; /*deletando antes para conseguir deletar em Carro */
DELETE FROM Carro WHERE id_carro = 2;
DELETE FROM piloto_equipamento WHERE id_piloto = 2;  #mesma coisa no de cima, deletando em baixo para conseguir deletar em Piloto#
DELETE FROM Piloto WHERE id_piloto = 2;

-- Consultas (com JOIN)
SELECT Carro.nome AS Carro, Marca.nome AS Marca, Piloto.nome AS Piloto
FROM Carro
JOIN Marca ON Carro.id_marca = Marca.id_marca
JOIN Carro_Piloto ON Carro.id_carro = Carro_Piloto.id_carro
JOIN Piloto ON Carro_Piloto.id_piloto = Piloto.id_piloto;

SELECT Marca.nome AS Marca, Patrocinador.nome AS Patrocinador
FROM Marca
JOIN Marca_Patrocinador ON Marca.id_marca = Marca_Patrocinador.id_marca
JOIN Patrocinador ON Marca_Patrocinador.id_patrocinador = Patrocinador.id_patrocinador;

SELECT Piloto.nome AS Piloto, Equipamento_Seguranca.nome AS Equipamento
FROM Piloto
JOIN Piloto_Equipamento ON Piloto.id_piloto = Piloto_Equipamento.id_piloto
JOIN Equipamento_Seguranca ON Piloto_Equipamento.id_equipamento = Equipamento_Seguranca.id_equipamento;

-- Views
DROP VIEW IF EXISTS CarrosComPilotos;
SELECT Carro.nome AS Carro, Marca.nome AS Marca, GROUP_CONCAT(Piloto.nome) AS Pilotos
FROM Carro
JOIN Marca ON Carro.id_marca = Marca.id_marca
JOIN Carro_Piloto ON Carro.id_carro = Carro_Piloto.id_carro
JOIN Piloto ON Carro_Piloto.id_piloto = Piloto.id_piloto
GROUP BY Carro.id_carro;

DROP VIEW IF EXISTS PatrocinadoresPorMarca;
SELECT Marca.nome AS Marca, GROUP_CONCAT(Patrocinador.nome) AS Patrocinadores
FROM Marca
JOIN Marca_Patrocinador ON Marca.id_marca = Marca_Patrocinador.id_marca
JOIN Patrocinador ON Marca_Patrocinador.id_patrocinador = Patrocinador.id_patrocinador
GROUP BY Marca.id_marca;

-- Triggers
DROP TRIGGER IF EXISTS before_insert_piloto;
DROP TRIGGER IF EXISTS after_delete_carro;

DELIMITER $$
SHOW TRIGGERS LIKE 'Piloto';

CREATE TRIGGER before_insert_piloto
BEFORE INSERT ON Piloto
FOR EACH ROW
BEGIN
    DECLARE count_pilotos INT;
    SELECT COUNT(*) INTO count_pilotos FROM Piloto WHERE nome = NEW.nome;
    IF count_pilotos > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Piloto já existe';
    END IF;
END;

CREATE TRIGGER after_delete_carro
AFTER DELETE ON Carro
FOR EACH ROW
BEGIN
    INSERT INTO Log (acao, descricao) VALUES ('DELETE', CONCAT('Carro ', OLD.nome, ' foi excluído.'));
END$$

DELIMITER ;
