use skymth_db;

CREATE TABLE `wano_intern` (
  id bigint unsigned NOT NULL AUTO_INCREMENT,
  create_time datetime NOT NULL,
  update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  report_date date NOT NULL,
  store_id int(10) unsigned NOT NULL,
  country_id int(10) unsigned NOT NULL,
  artist_id int(10) unsigned NOT NULL,
  release_id int(10) unsigned NOT NULL,
  song_id int(10) unsigned DEFAULT NULL,
  distribution_type tinyint(1) NOT NULL,
  total_quantity int(10)  NOT NULL,
  jpy_unit_price decimal(36,20) NOT NULL DEFAULT 0.00000000000000000000,
  jpy_total_price decimal(36,20) NOT NULL DEFAULT 0.00000000000000000000,
  PRIMARY KEY (id, report_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
