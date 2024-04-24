BEGIN;
--
-- Create model inicioPage
--
CREATE TABLE "inicio_iniciopage" ("page_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "wagtailcore_page" ("id") DEFERRABLE INITIALLY DEFERRED, "body" text NOT NULL, "imagenCarousel_id" integer NULL REFERENCES "wagtailimages_image" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "inicio_iniciopage_imagenCarousel_id_3239657e" ON "inicio_iniciopage" ("imagenCarousel_id");
COMMIT;
BEGIN;
--
-- Remove field body from iniciopage
--
ALTER TABLE "inicio_iniciopage" DROP COLUMN "body";
--
-- Remove field imagenCarousel from iniciopage
--
CREATE TABLE "new__inicio_iniciopage" ("page_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "wagtailcore_page" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__inicio_iniciopage" ("page_ptr_id") SELECT "page_ptr_id" FROM "inicio_iniciopage";
DROP TABLE "inicio_iniciopage";
ALTER TABLE "new__inicio_iniciopage" RENAME TO "inicio_iniciopage";
--
-- Add field carouselImages to iniciopage
--
CREATE TABLE "new__inicio_iniciopage" ("page_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "wagtailcore_page" ("id") DEFERRABLE INITIALLY DEFERRED, "carouselImages" text NOT NULL CHECK ((JSON_VALID("carouselImages") OR "carouselImages" IS NULL)));
INSERT INTO "new__inicio_iniciopage" ("page_ptr_id", "carouselImages") SELECT "page_ptr_id", '""' FROM "inicio_iniciopage";
DROP TABLE "inicio_iniciopage";
ALTER TABLE "new__inicio_iniciopage" RENAME TO "inicio_iniciopage";
--
-- Add field services to iniciopage
--
CREATE TABLE "new__inicio_iniciopage" ("page_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "wagtailcore_page" ("id") DEFERRABLE INITIALLY DEFERRED, "carouselImages" text NOT NULL CHECK ((JSON_VALID("carouselImages") OR "carouselImages" IS NULL)), "services" text NOT NULL CHECK ((JSON_VALID("services") OR "services" IS NULL)));
INSERT INTO "new__inicio_iniciopage" ("page_ptr_id", "carouselImages", "services") SELECT "page_ptr_id", "carouselImages", '""' FROM "inicio_iniciopage";
DROP TABLE "inicio_iniciopage";
ALTER TABLE "new__inicio_iniciopage" RENAME TO "inicio_iniciopage";
COMMIT;
