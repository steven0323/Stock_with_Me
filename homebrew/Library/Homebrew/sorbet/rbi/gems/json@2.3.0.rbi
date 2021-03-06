# This file is autogenerated. Do not edit it by hand. Regenerate it with:
#   tapioca sync

# typed: true

class Class < ::Module
  def json_creatable?; end
end

module JSON

  private

  def dump(obj, anIO = _, limit = _); end
  def fast_generate(obj, opts = _); end
  def fast_unparse(obj, opts = _); end
  def generate(obj, opts = _); end
  def load(source, proc = _, options = _); end
  def parse(source, opts = _); end
  def parse!(source, opts = _); end
  def pretty_generate(obj, opts = _); end
  def pretty_unparse(obj, opts = _); end
  def recurse_proc(result, &proc); end
  def restore(source, proc = _, options = _); end
  def unparse(obj, opts = _); end

  def self.[](object, opts = _); end
  def self.create_id; end
  def self.create_id=(_); end
  def self.deep_const_get(path); end
  def self.dump(obj, anIO = _, limit = _); end
  def self.dump_default_options; end
  def self.dump_default_options=(_); end
  def self.fast_generate(obj, opts = _); end
  def self.fast_unparse(obj, opts = _); end
  def self.generate(obj, opts = _); end
  def self.generator; end
  def self.generator=(generator); end
  def self.iconv(to, from, string); end
  def self.load(source, proc = _, options = _); end
  def self.load_default_options; end
  def self.load_default_options=(_); end
  def self.parse(source, opts = _); end
  def self.parse!(source, opts = _); end
  def self.parser; end
  def self.parser=(parser); end
  def self.pretty_generate(obj, opts = _); end
  def self.pretty_unparse(obj, opts = _); end
  def self.recurse_proc(result, &proc); end
  def self.restore(source, proc = _, options = _); end
  def self.state; end
  def self.state=(_); end
  def self.unparse(obj, opts = _); end
end

class JSON::GenericObject < ::OpenStruct
  def as_json(*_); end
  def to_hash; end
  def to_json(*a); end
  def |(other); end

  def self.dump(obj, *args); end
  def self.from_hash(object); end
  def self.json_creatable=(_); end
  def self.json_creatable?; end
  def self.json_create(data); end
  def self.load(source, proc = _, opts = _); end
end

class JSON::JSONError < ::StandardError
  def self.wrap(exception); end
end

JSON::Parser = JSON::Ext::Parser

JSON::State = JSON::Ext::Generator::State

JSON::UnparserError = JSON::GeneratorError

module Kernel

  private

  def JSON(object, *args); end
  def j(*objs); end
  def jj(*objs); end
end
