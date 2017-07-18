# -*- coding: utf-8 -*-
"""
@Time : 2017/7/17 16:20
@Author : Yu Yuan

"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.orm.state import InstanceState

db = SQLAlchemy()


# Model 序列化代码（转自flask-jsontools）
def get_entity_propnames(entity):
    """ Get entity property names
        :param entity: Entity
        :type entity: sqlalchemy.ext.declarative.api.DeclarativeMeta
        :returns: Set of entity property names
        :rtype: set
    """
    ins = entity if isinstance(entity, InstanceState) else inspect(entity)
    return set(
        ins.mapper.column_attrs.keys() +  # Columns
        ins.mapper.relationships.keys()  # Relationships
    )


def get_entity_loaded_propnames(entity):
    """ Get entity property names that are loaded (e.g. won't produce new queries)

        :param entity: Entity
        :type entity: sqlalchemy.ext.declarative.api.DeclarativeMeta
        :returns: Set of entity property names
        :rtype: set
    """
    ins = inspect(entity)
    keynames = get_entity_propnames(ins)

    # If the entity is not transient -- exclude unloaded keys
    # Transient entities won't load these anyway, so it's safe to include all columns and get defaults
    if not ins.transient:
        keynames -= ins.unloaded

    # If the entity is expired -- reload expired attributes as well
    # Expired attributes are usually unloaded as well!
    if ins.expired:
        keynames |= ins.expired_attributes

    # Finish
    return keynames


class JsonAble(object):
    """ Declarative Base mixin to allow objects serialization

        Defines interfaces utilized by :cls:ApiJSONEncoder
    """

    def __json__(self, exluded_keys=set()):
        return {name: getattr(self, name)
                for name in get_entity_loaded_propnames(self) - exluded_keys}
