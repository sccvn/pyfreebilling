/* add SANDBOX server as trusted source to used to be accepted by kamailio */
INSERT INTO address(id,grp,ip_addr,mask,port,tag) values (1,1,'20.110.145.242',32,5060,'SANDBOX');
INSERT INTO trusted(id,src_ip,proto,from_pattern,ruri_pattern,tag,priority) values (1,'20.110.145.242','udp',NULL,NULL,'SANDBOX',0);
/* UPDATE address SET port=32527 WHERE id=1; */

/* add SANDBOX DID +12542724613 in to dialplan */
INSERT INTO dialplan(id,dpid,pr,match_op,match_exp,match_len,subst_exp,repl_exp,attrs) values (1,1,0,0,'+12542724613',12,'\+','','FLAG_SANDBOX_DP');