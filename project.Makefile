## Add your own custom Makefile targets here

gen-project:
	$(RUN) gen-project ${CONFIG_YAML} -d $(DEST) $(SOURCE_SCHEMA_PATH)
