/* add SANDBOX server as trusted source to used to be accepted by kamailio */
INSERT INTO address(id,grp,ip_addr,mask,port,tag) values (1,1,'20.110.145.242',32,5060,'SANDBOX');
INSERT INTO trusted(id,src_ip,proto,from_pattern,ruri_pattern,tag,priority) values (1,'20.110.145.242','udp',NULL,NULL,'SANDBOX',0);
/* UPDATE address SET port=32527 WHERE id=1; */

/* add SANDBOX DID +12542724613 in to dialplan */
INSERT INTO dialplan(id,dpid,pr,match_op,match_exp,match_len,subst_exp,repl_exp,attrs) values (1,3,0,0,'+12542724613',12,'','','SANDBOX');
INSERT INTO dialplan(id,dpid,pr,match_op,match_exp,match_len,subst_exp,repl_exp,attrs) values (2,3,0,0,'+12312444852',12,'','','SANDBOX');
INSERT INTO dialplan(id,dpid,pr,match_op,match_exp,match_len,subst_exp,repl_exp,attrs) values (3,3,0,0,'64c101040e4bda5ad45f9c1b',24,'','','SANDBOX');
INSERT INTO dialplan(id,dpid,pr,match_op,match_exp,match_len,subst_exp,repl_exp,attrs) values (4,3,0,0,'+12542724631',12,'','','SANDBOX');

/* add SANDBOX DID 12542724631 to htable ~ tenant table */
INSERT INTO tenant(id,key_name,key_type,value_type,key_value,expires) VALUES (1,'64c780a60e4bda5ad45fa306',0,0,'+12542724613',0);
INSERT INTO tenant(id,key_name,key_type,value_type,key_value,expires) VALUES (2,'64c101040e4bda5ad45f9c1b',0,0,'64c101040e4bda5ad45f9c1b',0);
INSERT INTO tenant(id,key_name,key_type,value_type,key_value,expires) VALUES (3,'64c780a60e4bda5ad45fa406',0,0,'+12312444852',0);
INSERT INTO tenant(id,key_name,key_type,value_type,key_value,expires) VALUES (4,'64c780a60e4bda5ad45fa506',0,0,'+12542724631',0);
/* add dialplan to test with SANDBOX 20.110.145.242 */
/*
 * kamcmd dispatcher.add 3 sip:20.110.145.242:5060;transport=udp 0 0 duid=sandbox;socket:udp:20.110.145.242:5060;ping_from=apac.belltouch.xyz
 * kamcmd dispatcher.add 33 sip:20.110.145.242:5060 0 0 duid=sandbox;socket:udp:20.110.145.242:5060;ping_from=apac.belltouch.xyz
*/
