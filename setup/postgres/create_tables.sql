
CREATE TABLE public.devices
(
    device_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    signature text COLLATE pg_catalog."default" NOT NULL DEFAULT 'device'::text,
    ip inet NOT NULL DEFAULT '127.0.0.1'::inet,
    opts json NOT NULL DEFAULT '{}'::json,
    CONSTRAINT devices_pkey PRIMARY KEY (device_id)
);

CREATE TABLE public.telemetry
(
    telemetry_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    device_id bigint NOT NULL,
    temperature integer,
    pressure integer,
    moisture integer,
    luminosity integer,
    "timestamp" timestamp with time zone NOT NULL,
    CONSTRAINT telemetry_pkey PRIMARY KEY (telemetry_id),
    CONSTRAINT telemetry_device_id_fkey FOREIGN KEY (device_id)
        REFERENCES public.devices (device_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

