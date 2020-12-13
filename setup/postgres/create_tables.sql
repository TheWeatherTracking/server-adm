
CREATE TABLE public.devices
(
    device_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    signature text NOT NULL DEFAULT 'device'::text,
    ip text NOT NULL DEFAULT '127.0.0.1',
    props text NOT NULL DEFAULT '',
    CONSTRAINT devices_pkey PRIMARY KEY (device_id)
);
GRANT ALL PRIVILEGES ON TABLE public.devices TO dev;



CREATE TABLE public.telemetry
(
    telemetry_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    device_id bigint NOT NULL,
    temperature integer,
    pressure integer,
    moisture integer,
    luminosity integer,
    tmstamp timestamp with time zone NOT NULL,
    CONSTRAINT telemetry_pkey PRIMARY KEY (telemetry_id),
    CONSTRAINT telemetry_device_id_fkey FOREIGN KEY (device_id)
        REFERENCES public.devices (device_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
GRANT ALL PRIVILEGES ON TABLE public.telemetry TO dev;



CREATE TABLE public.users
(
    user_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    login text NOT NULL DEFAULT ''::text,
    password text NOT NULL DEFAULT ''::text,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);

GRANT ALL PRIVILEGES ON TABLE public.users TO dev;



