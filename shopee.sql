drop database if exists shopee;
create database if not exists shopee;

use shopee;

create table if not exists produto (
	id integer auto_increment,
    nome varchar(30) not null,
    preco numeric(5,2) not null,
    descricao varchar(100),
    primary key (id)
);

create table if not exists cliente (
	id integer auto_increment,
    nome varchar(50) not null,
    login varchar(30) not null,
    senha varchar(20) not null,
    primary key(id)
);

create table if not exists pedido (
	id integer auto_increment,
    id_cliente integer,
    id_produto integer,
    quantidade integer not null,
    primary key(id, id_cliente, id_produto),
    foreign key(id_cliente) references cliente(id),
    foreign key(id_produto) references produto(id)
);
