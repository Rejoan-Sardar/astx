"""Test callable ASTx objects."""

import astx

from astx.viz import visualize


def test_variable() -> None:
    """Test function creation with modifiers."""
    var_a = astx.Variable("a")

    assert str(var_a)
    assert var_a.get_struct()
    assert var_a.get_struct(simplified=True)

    visualize(var_a.get_struct())


def test_variable_decl() -> None:
    """Test function creation with modifiers."""
    decl_a = astx.VariableDeclaration(
        "a", type_=astx.Int32(), value=astx.LiteralInt32(1)
    )

    assert str(decl_a)
    assert decl_a.get_struct()
    assert decl_a.get_struct(simplified=True)

    visualize(decl_a.get_struct())


def test_inline_variable_decl() -> None:
    """Test function creation with modifiers."""
    decl_a = astx.InlineVariableDeclaration(
        "a", type_=astx.Int32(), value=astx.LiteralInt32(1)
    )

    assert str(decl_a)
    assert decl_a.get_struct()
    assert decl_a.get_struct(simplified=True)

    visualize(decl_a.get_struct())


def test_argument() -> None:
    """Test function creation with modifiers."""
    arg_a = astx.Argument(
        "a", type_=astx.Int32(), default=astx.LiteralInt32(1)
    )

    assert str(arg_a)
    assert arg_a.get_struct()
    assert arg_a.get_struct(simplified=True)

    visualize(arg_a.get_struct())


def test_arguments() -> None:
    """Test function creation with modifiers."""
    arg_a = astx.Argument(
        "a", type_=astx.Int32(), default=astx.LiteralInt32(1)
    )
    arg_b = astx.Argument(
        "b", type_=astx.Int32(), default=astx.LiteralInt32(2)
    )
    arg_c = astx.Argument(
        "c", type_=astx.Int32(), default=astx.LiteralInt32(3)
    )

    args = astx.Arguments(arg_a, arg_b)
    args.append(arg_c)

    assert str(args)
    assert args.get_struct()
    assert args.get_struct(simplified=True)

    visualize(args.get_struct())


def test_delete_stmt() -> None:
    """Test DeleteStmt creation and properties."""
    var1 = astx.Identifier(value="x")
    var2 = astx.Identifier(value="y")

    # Create a DeleteStmt with multiple values
    delete_stmt = astx.DeleteStmt(value=[var1, var2])

    # Test basic properties
    assert str(delete_stmt)
    assert delete_stmt.get_struct()
    assert delete_stmt.get_struct(simplified=True)

    # Visualize for documentation
    visualize(delete_stmt.get_struct())

    # Test with a single value
    single_delete = astx.DeleteStmt(value=[var1])
    assert str(single_delete)
    assert single_delete.get_struct()

    # Optional: visualize single value case too
    visualize(single_delete.get_struct())
